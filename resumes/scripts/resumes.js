var $ = jQuery.noConflict();

// Observer pattern taken from
// http://addyosmani.com/resources/essentialjsdesignpatterns/book/
function ObserverList(){
    this.observerList = [];
}

ObserverList.prototype.add = function( obj ){
    return this.observerList.push( obj );
};

ObserverList.prototype.count = function() {
    return this.observerList.length;
};

ObserverList.prototype.get = function( index ){
    if( index > -1 && index < this.observerList.length ){
        return this.observerList[ index ];
    }
};

ObserverList.prototype.indexOf = function( obj, startIndex ){
    var i = startIndex;

    while( i < this.observerList.length ){
        if( this.observerList[i] === obj ){
            return i;
        }
        i++;
    }
    return -1;
};

ObserverList.prototype.removeAt = function( index ){
    this.observerList.splice(index, 1);
};


function Subject(){
    this.observers = new ObserverList();
    this.lockedby = undefined;
}

Subject.prototype.addObserver = function( observer ){
    this.observers.add( observer );
};

Subject.prototype.removeObserver = function( observer ){
    this.observers.removeAt( this.observers.indexOf( observer, 0 ) );
};

Subject.prototype.notify = function( context ){
    var observerCount = this.observers.count();
    for(var i=0; i < observerCount; i++){
        this.observers.get(i).update( context );
    }
};

Subject.prototype.lock = function( who ){
    this.observers.removeAt( this.observers.indexOf( who, 0) );
    var observerCount = this.observers.count();
    for (var i=0; i < observerCount; i++){
        this.observers.get(i).lock();
    }
    this.observers.add( who );
    this.lockedby = who;
};


function Observer() {
    this.lock = function() {
    };
}


function EditList() {
    this.current = undefined;
    this.edits = [];
}

EditList.prototype.add = function( edit ) {
    if (this.current > 0) {
        this.edits.splice(this.current, this.edits.length - this.current);
    }
    this.edits.push(edit);
    if ( this.current === undefined ) {
        this.current = 1;
    } else {
        this.current += 1;
    }
};

EditList.prototype.undo = function() {
    if (this.current > 0) {
        this.current -= 1;
        return this.edits[this.current];
    } else {
        return undefined;
    }
};

EditList.prototype.redo = function() {
    if(this.current < this.edits.length-1) {
        this.current += 1;
        return this.edits[this.current];
    } else {
        return undefined;
    }
};

function ObjectEdits() {
    this.selector = undefined;
    this.edits = new EditList();
}

ObjectEdits.prototype.add = function( edit ) {
    this.edits.add(edit);
};

ObjectEdits.prototype.undo = function() {
    return this.edits.undo();
};

ObjectEdits.prototype.redo = function() {
    return this.edits.redo();
};

function EditManager() {
    this.editObjs = [];
    this.editReferences = [];
    this.current = undefined;
}

EditManager.prototype.get = function(selector){
    for (var i=0; i<this.editObjs.length; i++) {
        if (this.editObjs[i].selector === selector) {
            return this.editObjs[i];
        }
    }
    var obj = new ObjectEdits();
    obj.selector = selector;
    this.editObjs.push(obj);
    return obj;
};

EditManager.prototype.addEdit = function(selector, edit){
    editObj = this.get( selector );
    editObj.add( edit );
    this.editReferences.push( selector );
    if (this.current === undefined) {
        this.current = 1;
    } else {
        this.current += 1;
    }
};

EditManager.prototype.applyEdits = function( selector, edits ){
    ed = rGet(selector, 'editables');
    if (typeof edits === 'undefined' || edits.length === 0) {
        return;
    }
    for (var i=0; i< edits.length; i++){
        var elem;
        var idx = edits[i].index;
        if (ed[idx].selector !== undefined) {
            elem = $(selector).find(ed[idx].selector);
        } else {
            elem = selector;
        }
        if (elem.length > 1) {
            throw "Element editables not unique!";
        }
        ed[idx].setter(elem, edits[i].new_value);
    }
};

EditManager.prototype.undo = function() {
    if (this.current > 0 ) {
        this.current -= 1;
        lastEdit = this.editReferences[this.current];
        this.applyEdits( lastEdit, this.get(lastEdit).undo() );
    }
};

EditManager.prototype.redo = function() {
    if (this.current < this.editReferences.length) {
        this.current += 1;
        nextEdit = this.editReferences[this.current];
        this.applyEdits( nextEdit, this.get(nextEdit).redo() );
    }
};


MainActor = function( element, form, action, direction ){
    direction = typeof direction !== 'undefined' ? direction : true;
    var ed = rGet(element, 'editables');
    var ff = rGet(element, 'form_fields');
    var tweaks;
    var to_return;
    var edited;

    if (action === 'fill') {
        tweaks = rGet(element, 'tweaks');
    }
    if (action === 'changes') {
        edited = [];
    }

    if (ed.length != ff.length) {
        throw "Element editables and form_fields not the same size";
    }

    for (var i=0; i < ed.length; i++) {
        var elem;
        if (ed[i].selector !== undefined) {
            elem = $(element).find(ed[i].selector);
        } else {
            elem = element;
        }
        if (elem.length > 1) {
            throw "Element editables not unique!";
        }
        var field = $(form).find(ff[i].selector);
        if(field.length > 1) {
            throw "Form fields not unique!";
        }
        field = field[0];

        switch(action) {
            case 'fill' :
                {
                    if (direction) {
                        ff[i].setter(field, ed[i].getter(elem));
                        tweaks[i](elem, form);
                    } else {
                        ed[i].setter(elem, ff[i].getter(field));
                    }
                }
                break;
            case 'changes' :
                {
                    if (ff[i].getter(field) !== ed[i].getter(elem)) {
                        edited.push({'index':i, 'new_value': ff[i].getter(field)});
                    }
                }
                break;
            default:
                {}
        }
    if (action === 'changes') {
        to_return = edited;
    }
    if (typeof to_return !== 'undefined') {
        return to_return;
    }
    }
};

var fillForm = function(element, form, direction) {
    MainActor(element, form, 'fill', direction);
};

var formEdited = function(element, form) {
    return MainActor(element, form, 'changes');
};


function extend( extension, obj ){
    for ( var key in extension ){
        obj[key] = extension[key];
    }
}

var Sections = {
    'selector' : "[id^=section_]",
    'form_getter' : "#section_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ''
};
var cvEntries = {
    'selector' : "[id^=cventry_]",
    'form_getter' : "#cventry_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ''
};

var cvListItems = {
    'selector' : "[id^=cvlistitem_]",
    'form_getter' : "#cvlistitem_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ['textarea']
};
var cvColumns = {
    'selector' : "[id^=cvcolumn_]",
    'form_getter' : "#cvcolumn_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ''
};
var cvColumnItems = {
    'selector' : "[id^=cvcolumn_item_]",
    'form_getter' : "#cvcolumnitem_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ''
};
var cvItemHeadings = {
    'selector' : "[id^=cvitemized_heading_]",
    'form_getter' : "#cvitemized_heading_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ''
};
var cvItemizedItems = {
    'selector' : "[id^=cvitemized_item_]",
    'form_getter' : "#cvitemized_item_form",
    'edit_targets' : ["div.section.description"],
    'form_prefil' : ['textarea'],
    'editables' : [ { 
        'selector' : undefined,
        'setter' : function(elem, new_value) {
            elem.innerText = new_value;
        },
        'getter' : function(elem) {
            return elem.innerText;
        }
    }],
    'form_fields' : [ {
        'selector' : 'textarea',
        'setter' : function(elem, new_value) {
            $(elem).click();
            $(elem).focus();
            elem.value = $.trim(new_value);
            elem.defaultValue = $.trim(new_value);
            elem.text = $.trim(new_value);
            elem.innerText = $.trim(new_value);
            $(elem).val($.trim(new_value));
        },
        'getter' : function(elem) {
            return $(elem).val();
        },
    }],
    'tweaks' : [ function(elem, form) {
        var width = $(elem).parent().css('width');
        width = parseInt(width.replace('px','')) -1 + "px";
        $(form).find('textarea').css('width', width);
        $(form).find('textarea').autosize();
    } ]
};

var resumeElementType = function(elem) {
    for (var section in resumeIndex) {
        if ($(elem).is(resumeIndex[section].selector)){
            return section;
        }
    }
};


var resumeIndex = {
    'section' : Sections,
    'cventry' : cvEntries,
    'cvlistitem' : cvListItems,
    'cvcolumn' : cvColumns,
    'cvcolumnitem' : cvColumnItems,
    'cvitemheading' : cvItemHeadings,
    'cvitemizeditem' : cvItemizedItems
};

var rGet = function(elem, attrib) {
    obj = resumeIndex[resumeElementType(elem)];
    if (attrib in obj) {
        return obj[attrib];
    }
};



var getForm  = function(elem){
    var form_getter = resumeIndex[resumeElementType(elem)].form_getter;
    var form = document.createElement("div");
    // Right, I know that space looks wrong, but it's not.
    // Leave it alone, Arcidy
    $(form).load("/forms/resume_edit " + form_getter, populateForm(elem));
    $(form).attr("id", "form_" + $(elem).attr("id"));
    return form;
};

var populateForm = function(elem){
    return function(resp, status, xhr) {
        // and it seemed appropriate, even though it makes no sense
        // based on calling context.  Thanks Obama.
        fillForm(elem, this);
    };
};

var editBehavior = { 
    'trigger' : {'method' : 'click'},
    'actions' : function(elem, subj) {
        return function() {
            // onclick
            // hide this element and set the editlock
            $(elem).hide();
            subj.lock(elem);
            // get the form and prefill it
            var form = $("[id=form_"+$(elem).attr("id")+"]");
            if (form.length === 0) {
                form = getForm(elem);
                $(elem).after(form);
            } else {
                fillForm(elem, form);
            }           
            // display the form
            $(form).show();
            $('textarea').autosize();
        };
    },
    'last' : function(elem, subj) {
        // display the element one more
        $(elem).css("color", "purple");
        $(elem).show();
        // find the form
        var form = $("[id=form_"+$(elem).attr("id")+"]");
        // Need to transfer data from form to element
        // and hide it
        if (form.length > 0) {
            edits = formEdited(elem, form);
            if (edits.length > 0) {
                subj.addEdit(elem, edits);
            }
            fillForm(elem, form, false);
            form.hide();
        }
    },
    'init' : function(elem, subj) {
        $(elem).unbind('click');
        $(elem)[this.trigger.method](this.actions(elem, subj));
    }
};


var buttonStyle = function (button) {
    $(button).attr('href','#');
    $(button).css({"color": 'white',
        "background-color": '#F33333',
        'text-decoration': 'none',
        'font-weight': 'bold',
        'padding': '2px',
        'margin': '0px 2px'
    });
};


var editMenu = function(editmanager) {
    menu = document.createElement("div");
    $(menu).attr('class', 'editmenu');
    undo = document.createElement("a");
    $(undo).text("Undo");
    $(undo).click( function() {
            editmanager.undo();
        });
    buttonStyle(undo);
    $(menu).append(undo);

    redo = document.createElement("a");
    $(redo).text("Redo");
    $(redo).click( function() {
        editmanager.redo();
    });
    buttonStyle(redo);
    $(menu).append(redo);

    $(menu).css({'position': 'fixed',
        'right': '5px',
        'top': '5px',
        'width': '200px',
        'height': '40px'
    });
    $('body').append(menu);
};

$(document).ready(function(){
    var sections = $("[id^=section]");
    var cvitemizeditems = $("[id^=cvitemized_item]");
    var ebs = editBehavior;
    var elem = $("[id=cvitemized_item_5]")[0];


    for (var i=0; i < sections.length; i++) {
        //x.init(sections[i]);
    }

    // Instanciate a Subject for observer pattern
    var subj = new Subject();
    extend( new EditManager(), subj );

    // Need instanciated variables to populate
    // subject's unlock function
    subj.unlock = function(){
        var observerCount = this.observers.count();
        for (var i=0; i < observerCount; i++){
            obs = this.observers.get(i);
            $(obs).unbind('click');
            $(obs)[ebs.trigger.method](ebs.actions(obs, subj));
        }
        ebs.last(this.lockedby, this);
        this.lockedby = undefined;
    };

    // Need instanciated subject for observer's
    // lock function
    // And js doesn't like creating functions in a loop
    function lockObject(obj, subj) {
        obj.lock = function() {
            $(obj).unbind('click');
            $(obj).click( function() {
                subj.unlock();
            });
        };
    }

    // Instrument all the items as observers and
    // editable items
    for (i=0; i < cvitemizeditems.length; i++){
        item = cvitemizeditems[i];
        ebs.init(item, subj);
        extend(new Observer(), item);
        lockObject(item, subj);
        subj.addObserver(item);
    }

   editMenu(subj); 
}
);
