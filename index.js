// Need $.when to get both files.
$.when(
    $.ajax("python/dataTerm.json"),
    $.ajax("python/dataSubject.json")
). done(function(term, subject) {
    console.log(term[0,1]);
    console.log(subject[0]);
})