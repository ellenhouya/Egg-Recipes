function numberKeyValuePairs(obj) {
  let object = obj;

  // Get the number of key-value pairs in the ingredientsMeasuers object
  let numPairs = Object.keys(object).length;

  return numPairs;
}

function renderIngredientsAndMeasures(object, parent, keyId, valId) {
  // Get the keys of the object
  let keys = Object.keys(object);

  // Iterate over the keys
  keys.forEach((key, index) => {
    // Get the value corresponding to the key
    let value = object[key];

    // Find the corresponding input fields by their IDs
    let ingredientField = $(parent).find(keyId).eq(index);
    let measureField = $(parent).find(valId).eq(index);

    // Set the values of the input fields
    if (ingredientField.length > 0 && measureField.length > 0) {
      ingredientField.val(key);
      measureField.val(value);
    }
  });
}

$(document).ready(function () {
  for (let key in selectedMeal) {
    if (selectedMeal.hasOwnProperty(key)) {
      let value = selectedMeal[key];

      let inputField = $("#" + key);

      if (inputField.length > 0) {
        inputField.val(value);
      }
    }
  }

  // ingredients object
  // Get the number of key-value pairs in the ingredientsMeasuers object
  let ingNumPairs = numberKeyValuePairs(selectedMeal.ingredientsMeasuers);

  for (i = 0; i < ingNumPairs - 1; i++) {
    addFields(".ingredients-measures", ".ing-measures-con");
  }

  let nutritionNumPairs = numberKeyValuePairs(selectedMeal.nutritionFacts);

  for (i = 0; i < nutritionNumPairs - 1; i++) {
    addFields(".nutrition-facts", ".nutrition-facts-con");
  }

  // render ingredient object
  renderIngredientsAndMeasures(
    selectedMeal.ingredientsMeasuers,
    ".ingredients-measures",
    "#ingredients",
    "#measures"
  );

  // render nutrition object
  renderIngredientsAndMeasures(
    selectedMeal.nutritionFacts,
    ".nutrition-facts",
    "#nutrition",
    "#amount"
  );

  // submit edit
  $("form").submit(function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    var action = $(this).attr("action");
    if (action === "/edit") {
      // Serialize form data into a JSON object
      var formData = serializeFormData();

      // find IdMeal
      var idMeal = getIdMeal();

      formData.idMeal = idMeal;

      formData.rating = parseInt(formData.rating);

      $.ajax({
        type: "POST",
        url: "/edit/<id>",
        data: JSON.stringify(formData),
        contentType: "application/json",
        success: function (response) {
          window.location.href = `/view/${response.idMeal}`;
        },
        error: function (error) {
          // Handle the error response here
          console.error(error);
        },
      });
    }
  });

  // discard changes
  $("#edit-data-discard-btn").click(function () {
    showMessage("#confirmMessage");

    $("#see-result-btn").click(function () {
      removeLayer(".content-before");
      removeLayer(".nav-con-before");
      window.location.href = `/view/${getIdMeal()}`;
    });

    $("#complete-q-btn").click(function () {
      removeLayer(".content-before");
      removeLayer(".nav-con-before");
      $("#confirmMessage").removeClass("show");
    });
  });
});

function getIdMeal() {
  var currentUrl = window.location.href;

  var urlParts = currentUrl.split("/");

  // Extract the part containing "03"
  return urlParts[urlParts.length - 1];
}
