var my_view = new ol.View({
  center: ol.proj.fromLonLat([-122.394984, 37.794118]),
  zoom:10
});

function init(){
  var map=new ol.Map({
    target:'map',
    layers:[
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view:my_view
  });
}

function panHome() {
  my_view.animate({
    center: ol.proj.fromLonLat([-122.394962, 37.794006]),
    duration:2000
  })
}

function myFav() {
  my_view.animate({
    center:ol.proj.fromLonLat([33.6846,117.8265]),
    duration: 2000
  })
}




window.onload=init;
