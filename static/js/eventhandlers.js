
/* This file handles all incoming events from the html-view.
Every click, dialog or alert needs to be triggered here, whereas the function need to be
implemented in separated .js-files.

TODO: Outsource the open-dialog function to readfiles.js
*/

// this is a placeholder event for the top level domain filter
var tldbutton = document.getElementById('topLevelDomainFilter');
    tldbutton.onclick = function(){
    alert('I am the TLD-Filter');
};

// this is a placeholder event for the statuscode filter
var statusbutton = document.getElementById('statusCodeFilter');
statusbutton.onclick = function(){
    alert('I am the statuscode filter');
};

// this is a placeholder event for the export functionality
var exportbutton = document.getElementById('exportView');
exportbutton.onclick = function(){
    alert('I am exporting the current view!');
};

// this is a placeholder event for the reset functionality
var resetbutton = document.getElementById('resetView');
resetbutton.onclick = function(){
    alert('I am reseting the view and removing all filters');
};