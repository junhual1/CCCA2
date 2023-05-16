// agism --- new-view
function (doc) {
  emit([doc.state,doc.SUA_NAME], {ageing_population: doc.ageing_population, ageing_population_percentage: doc.ageing_population_percentage});
}

// sexism --- new-view
function (doc) {
  emit([doc.state,doc.SUA_NAME], {males: doc.males, females: doc.females, gender_ratio: doc.gender_ratio});
}

// unemployment --- new-view
function (doc) {
  emit([doc.state,doc.SUA_NAME], {people_employed: doc.people_employed, employment_rate: doc.employment_rate});
}