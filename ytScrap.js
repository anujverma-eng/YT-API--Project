function ytscrape() {

    var sh1 =  SpreadsheetApp.getActiveSpreadsheet().getSheetByName('RunScript');
    var keyword = sh1.getRange("B1").getValue();
   
    var results = YouTube.Search.list('id,snippet',{q:keyword,maxResults:500});
   
    var items = results.items.map(function(e){
      return[
      e.snippet.channelId,
      e.snippet.channelTitle,
      e.snippet.title,
      e.id.videoId,
      e.snippet.publishedAt
      ]
    })
    sh1.getRange(4, 1, items.length, items[0].length).setValues(items)  
   }
   