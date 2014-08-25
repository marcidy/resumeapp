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
};


function Observer() {
    this.lock = function() {
    };
}

function unLockSubject(elem, subj) {
    elem.unlock = function() {
        $(elem).unbind('click');
        $(elem).click(function() {
            subj.unlock();
        });
    };
}


function lockObject(obj, subj) {
    obj.lock = function() {
        $(obj).unbind('click');
        $(obj).click( function() {
            subj.unlock();
        });
    };
}
        

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
    'form_prefil' : ['textarea']
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
    $(form).load("/forms/resume_edit " + form_getter, populateForm(elem));
    $(form).attr("id", "form_" + $(elem).attr("id"));
    // FIXME:
    // callback fires before form_getter selector
    // Add form_getter to populate form as well
    return form;
};

var populateForm = function(elem){
    return function(resp, status, xhr) {
        var form_getter = rGet(elem, 'form_getter');
        var selectors = rGet(elem, 'form_prefil');
        var data = ['nothing'];
        for (var i=0; i < selectors.length; i++) {
            // get form.getter
            // use it on resp because callback fires
            // before form_getter in getForm is applied
            var test = $(resp).find(form_getter)[0];
            var obj = $(test).find(selectors[i])[0];
            var stuff = $(elem).val();
            $(obj).val($(elem).val());
        }
    };
};

var editMenus = { 
    'trigger' : {'method' : 'click'},
    'actions' : function(elem, subj) {
        return function() {
            $(elem).hide();
            subj.lock(elem);
            var selectors = resumeIndex[resumeElementType(elem)].form_prefil;
            var accessors = ['html'];
            var data = ["testicles"];
            var form = $("[id=form_"+$(elem).attr("id")+"]");
            if (form.length === 0) {
                form = getForm(elem);
                $(elem).after(form);
            }
            $(form).show();
            // $(form)[editMenus.end.method](editMenus.last(elem));
        };
    },
    'end' : {'method' : 'mouseout'},
    'last' : function(elem) {
        return function() {
            $(elem).css("color", "purple");
            $(elem).show();
            var form = $("[id=form_"+$(elem).attr("id")+"]");
            if (form.length > 0) {
                form.hide();
            }
        };
    },
    'init' : function(elem, subj) {
        $(elem).unbind('click');
        $(elem)[editMenus.trigger.method](editMenus.actions(elem, subj));
    }
};


$(document).ready(function(){
    var sections = $("[id^=section]");
    var cvitemizeditems = $("[id^=cvitemized_item]");
    var x = editMenus;
    var elem = $("[id=cvitemized_item_5]")[0];
    var g = document.createElement("div");
    $(g).append(document.createElement("textarea"));
    var ta = $(g).find('textarea')[0];
    ta.cols = "80";
    ta.rows = "1";
    $(g).find('textarea')[0].defaultValue = elem.innerText;
    $(elem).after(g);


    for (var i=0; i < sections.length; i++) {
        //x.init(sections[i]);
    }

    var subj = new Subject();

    subj.unlock = function(){
        var observerCount = this.observers.count();
        for (var i=0; i < observerCount; i++){
            obs = this.observers.get(i);
            $(obs).unbind('click');
            x.init(obs, subj);
        }
    };

    for (i=0; i < cvitemizeditems.length; i++){
        item = cvitemizeditems[i];
        x.init(item, subj);
        extend(new Observer(), item);
        unLockSubject(item, subj);
        lockObject(item, subj);
        subj.addObserver(item);
    }
}
);
