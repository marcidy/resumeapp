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

function Observer() {
    this.update = function () {
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
    'form_prefil' : ''
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
    'form_prefil' : ''
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

var getForm  = function(elem){
    var indexItem = resumeElementType(elem);
    var resumeIndexItem = resumeIndex[indexItem];
    var form_getter = resumeIndex[resumeElementType(elem)].form_getter;
    var form = document.createElement("div");
    form.id = "form_" + elem.id;
    $(form).load("/forms/resume_edit " + form_getter);
    return form;
};

    

var editMenus =  {
    'trigger' : {'method' : 'click'},
    'actions' : function(elem) {
        return function() {
            $(elem).css("color", "green");
        };
    },
    'end' : {'method' : 'blur'},
    'last' : function(elem) {
        return function() {
            $(elem).css("color", "purple");
        };
    },
    'init' : function(elem) {
        $(elem)[editMenus.trigger.method](editMenus.actions(elem));
        $(elem)[editMenus.end.method](editMenus.last);
    }
};


$(document).ready(function(){
    var x = editMenus;
    var sections = $("[id^=section_]");
    var cventries = $("[id^=cventry_]");
    var cvlistitems = $("[id^=cvlistitem_]");
    var cvcolumns = $("[id^=cvcolumn_]");
    var cvcolumitems = $("[id^=cvcolumn_item_]");
    var cvitemheadings = $("[id^=cvitemized_heading_]");
    var cvitemizeditems = $("[id^=cvitemized_item_]");
    var cvcolumngroup = $("[id^=cvcolumngroup_]");

    elem = $("[id=cvitemized_item_5]");
    form = getForm(elem);
    $(elem).after(form);

    for (var i=0; i < sections.length; i++) {
        //x.init(sections[i]);
    }

    for (i=0; i < cvitemizeditems.length; i++){
          x.init(cvitemizeditems[i]);
    }
}
);
