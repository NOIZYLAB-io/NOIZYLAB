/*
iZo Docs 1.0
Copyright (c) 2015 iZotope, Inc.
*/

function setMainFrameSrc() {
	var defaultPage = document.getElementById('mainFrame').src;
	var srcURL = GetURLParameter("src");
	if (srcURL == null) {
		srcURL = defaultPage;
	}
    document.getElementById('mainFrame').src = srcURL+window.location.hash;
    
    //now set the width too
	var browserWidth = window.innerWidth || document.body.clientWidth;
	var browserHeight = window.innerHeight || document.body.clientHeight;
	//left column is 265px wide, so subtract that from browser width
	document.getElementById('mainFrame').width = browserWidth - 265 + "px";
	document.getElementById('mainFrame').style.position = "absolute";
	document.getElementById('mainFrame').style.left = "265px";
	document.getElementById('mainFrame').height = browserHeight - 70 + "px";
	document.getElementById('tocFrame').height = browserHeight - 70 + "px";
};   

function GetURLParameter(sParam) {
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) {
            return sParameterName[1];
        }
    }
};

function setFrameDimensions() {
	var browserWidth = window.innerWidth || document.body.clientWidth;
	var browserHeight = window.innerHeight || document.body.clientHeight;
	//left column is 265px wide, so subtract that from browser width
	document.getElementById('mainFrame').width = browserWidth - 265 + "px";
	document.getElementById('mainFrame').height = browserHeight - 75 + "px";
	document.getElementById('tocFrame').height = browserHeight - 75 + "px";
};