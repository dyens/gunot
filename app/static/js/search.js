/*
 * search.js
 * Copyright (C) 2015 dyens <dyens@dyens>
 *
 * Distributed under terms of the MIT license.
 */
$(document).ready(function () {
    $('#author').tokenfield({
        autocomplete: {
            //source: ['red','blue','green','yellow','violet','brown','purple','black','white'],
            source: function(request, response){
                $.ajax({
                    type: "POST",
                    url: "search_service",
                    data: JSON.stringify({
                        get: 'get_sheet_author',
                        request: request.term
                    }, null, '\t'),
                    contentType: "application/json;charset=utf-8",
                    success: function (msg) {
                        response(msg.response);
                    },
                    // TODO: if debug == False - return None
                    error: function (msg) {
                        alert(msg.status + ' ' + msg.statusText);
                    }
                })
             },
            delay: 100
            },
        limit: 1,
    //max num of tokens
    });

    $('#arranger').tokenfield({
        autocomplete: {
            //source: ['red','blue','green','yellow','violet','brown','purple','black','white'],
            source: function(request, response){
                $.ajax({
                    type: "POST",
                    url: "search_service",
                    data: JSON.stringify({
                        get: 'get_sheet_arranger',
                        request: request.term
                    }, null, '\t'),
                    contentType: "application/json;charset=utf-8",
                    success: function (msg) {
                        response(msg.response);
                    },
                    // TODO: if debug == False - return None
                    error: function (msg) {
                        alert(msg.status + ' ' + msg.statusText);
                    }
                })
             },
            delay: 100
            },
    //max num of tokens
    });
    $('#instrument').tokenfield({
        autocomplete: {
            //source: ['red','blue','green','yellow','violet','brown','purple','black','white'],
            source: function(request, response){
                $.ajax({
                    type: "POST",
                    url: "search_service",
                    data: JSON.stringify({
                        get: 'get_sheet_instrument',
                        request: request.term
                    }, null, '\t'),
                    contentType: "application/json;charset=utf-8",
                    success: function (msg) {
                        response(msg.response);
                    },
                    // TODO: if debug == False - return None
                    error: function (msg) {
                        alert(msg.status + ' ' + msg.statusText);
                    }
                })
             },
            delay: 100
            },
    //max num of tokens
    });
    $('#instrument').tokenfield('writeable')
});

