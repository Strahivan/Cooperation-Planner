
/* This file handles all incoming events from the html-view.
Every click, dialog or alert needs to be triggered here, whereas the function need to be
implemented in separated .js-files.

TODO: Outsource the open-dialog function to readfiles.js
*/


// dialogbox after click on first input button on index.html
var csvuploadbutton = document.getElementById('inputbutton');
csvuploadbutton.onclick = function(){
var csvupload = $(document.createElement("input"));
csvupload.attr("type", "file");
csvupload.trigger("click");
};

// this is a placeholder event for the top level domain filter
var tldbutton = document.getElementById('topleveldomainfilter');
tldbutton.onclick = function(){
alert('I am the TLD-Filter');
};

// this is a placeholder event for the statuscode filter
var statusbutton = document.getElementById('statuscodefilter');
statusbutton.onclick = function(){
alert('I am the statuscode filter');
};

// this is a placeholder event for the export functionality
var exportbutton = document.getElementById('exportview');
exportbutton.onclick = function(){
alert('I am exporting the current view!');
};

// this is a placeholder event for the reset functionality
var resetbutton = document.getElementById('resetview');
resetbutton.onclick = function(){
alert('I am reseting the view and removing all filters');
};