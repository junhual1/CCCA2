// geocenter --- new-view
function (doc) {
    emit(doc.name, {lat: doc.lat, lng: doc.lng});
}