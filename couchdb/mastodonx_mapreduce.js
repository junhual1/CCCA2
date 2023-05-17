// agism --- new-view
//// Map
function (doc) {
    var keywords = ['aging population','senior citizens','gerontology','age-related','retire',
    'longevity','ageism','elderly','silver economy','age-friendly','age discrimination','elder abuse','annuation',
    'pension','senile','nursing home', 'rest home','endowment insurance','aging care','old-age','old age'];
    if (doc.content) {
        var found = {};
        for (var i = 0; i < keywords.length; i++) {
            if (doc.content.toLowerCase().includes(keywords[i])) {
                found[keywords[i]] = true;
            }
        }
        if (Object.keys(found).length > 0) {
            emit('agism', {total: 1, mentioned:1});
        } else{
            emit('agism', {total: 1, mentioned:0});
        }
    } else {
        emit('agism', {total: 1, mentioned:0});
    }
}
//// Reduce
function (keys, values, rereduce) {
    var result = { total: 0, mentioned: 0, percentage: 0};

    for (var i = 0; i < values.length; i++) {
        result.total += values[i].total;
        result.mentioned += values[i].mentioned;
    }
    result.percentage = result.mentioned / result.total * 100;

    return result;
}

// sexism --- new-view
//// Map
function (doc) {
    var keywords = ['gender discrimination','sexism','gender bias','sexual harassment','glass ceiling','pay gap',
    "women's rights",'feminis','gender inequality','male privilege','woman security','women in leadership','gender stereotypes',
    'gender roles','gender-based violence','sexual violence','misogyny','gender issue','metoo','timesup','believewomen',
    'toxicMasculinity','genderequality','equalpay','endrapeculture','menomore','notallmen','maleprivilege','girlpower',
    'sexualharassment','consentmatters','consent matter'];
    if (doc.content) {
        var found = {};
        for (var i = 0; i < keywords.length; i++) {
            if (doc.content.toLowerCase().includes(keywords[i])) {
                found[keywords[i]] = true;
            }
        }
        if (Object.keys(found).length > 0) {
            emit('sexism', {total: 1, mentioned:1});
        } else{
            emit('sexism', {total: 1, mentioned:0});
        }
    } else {
        emit('sexism', {total: 1, mentioned:0});
    }
}
//// Reduce
function (keys, values, rereduce) {
    var result = { total: 0, mentioned: 0, percentage: 0};

    for (var i = 0; i < values.length; i++) {
        result.total += values[i].total;
        result.mentioned += values[i].mentioned;
    }
    result.percentage = result.mentioned / result.total * 100;

    return result;
}

// unemployment --- new-view
//// Map
function (doc) {
    var keywords = ['got fired','employ','idle','job loss',' layoff','jobless','redundancy',
    'furlough','downsizing','out of work','retrenchment','job hunt',
    'career transition','job market','job search','job seeker','jobkeeper','hiring'];
    if (doc.content) {
        var found = {};
        for (var i = 0; i < keywords.length; i++) {
            if (doc.content.toLowerCase().includes(keywords[i])) {
                found[keywords[i]] = true;
            }
        }
        if (Object.keys(found).length > 0) {
            emit('unemployment', {total: 1, mentioned:1});
        } else{
            emit('unemployment', {total: 1, mentioned:0});
        }
    } else {
        emit('unemployment', {total: 1, mentioned:0});
    }
}
//// Reduce
function (keys, values, rereduce) {
    var result = { total: 0, mentioned: 0, percentage: 0};

    for (var i = 0; i < values.length; i++) {
        result.total += values[i].total;
        result.mentioned += values[i].mentioned;
    }
    result.percentage = result.mentioned / result.total * 100;

    return result;
}