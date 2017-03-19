// Need $.when to get both files.
$.when(
    $.ajax("dataTerm.json"),
    $.ajax("dataSubject.json")
). done(function(term, subject) {
    console.log(term[0]);
    console.log(subject[0]);
})