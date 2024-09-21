const popular3Recipes = [
  {
    idMeal: "01",
    mealName: "Blini Pancakes",
    mealThumb:
      "https://www.themealdb.com/images/media/meals/0206h11699013358.jpg",
    rating: 5,
    calLevel: "Low",
    area: "Russian",
    category: ["Side", "Dessert"],
  },
  {
    idMeal: "03",
    mealName: "Apple Crumble",
    mealThumb:
      "https://www.themealdb.com/images/media/meals/xvsurr1511719182.jpg",
    rating: 4,
    calLevel: "Moderate",
    area: "British",
    category: ["Side", "Dessert"],
  },
  {
    idMeal: "05",
    mealName: "Bread Omelette",
    mealThumb:
      "https://www.themealdb.com/images/media/meals/hqaejl1695738653.jpg",
    rating: 4,
    calLevel: "High",
    area: "Irish",
    category: ["Breakfast", "Lunch"],
  },
];

function highlightMatch(text, input) {
  if (!input) return text;

  // Split the input string into individual terms
  const terms = input.split(",").map((term) => term.trim());

  // Iterate over each term and apply highlighting
  terms.forEach((term) => {
    const regex = new RegExp(term, "gi");
    text = text.replace(
      regex,
      '<span style="color: black; background-color: yellow;">$&</span>'
    );
  });

  return text;
}

function displayRecipes(recipes, input = null) {
  $(".row.gx-1").empty();

  for (let i = 0; i < recipes.length; i++) {
    let stars = "";
    for (let j = 0; j < recipes[i].rating; j++) {
      stars += "&#9733;"; // Add a star for each rating value
    }

    const highlightedMealName = highlightMatch(recipes[i].mealName, input);
    const highlightedCalLevel = highlightMatch(recipes[i].calLevel, input);
    const highlightedArea = highlightMatch(recipes[i].area, input);

    const categoryLinks = recipes[i].category
      .map(
        (category) =>
          `<a href="/display_filter_results?checkedVals=${category}" class="${category}-text highlighted">${highlightMatch(
            category,
            input
          )}</a>`
      )
      .join(" | ");

    $(".row.gx-1").append(`
        <div class="col-md-4">
          <div class="card">
            <div class="card-img-title">
              <a href="/view/${recipes[i].idMeal}">
                <img
                  src="${recipes[i].mealThumb}"
                  class="card-img-top"
                  alt="${recipes[i].mealName}"
                />
              </a>  
              <div class="card-name-rating">
                <h5 class="recipe-name">${highlightedMealName}</h5>
                <span class="rating-stars">${stars}</span>
                <div class="card-body">
                  <p class="card-text"><a href="/display_filter_results?checkedVals=${recipes[i].calLevel}" class="cal-text highlighted">${highlightedCalLevel}</a> Calorie</p>
                  
                  <p class="card-area"><a href="/display_filter_results?checkedVals=${recipes[i].area}" class="cuisine-text highlighted">${highlightedArea}</a> Cuisine</p>
                  <p class="card-category">${categoryLinks}</p>
                </div>
              </div>
            </div>
            <div class="message-con">
              <a class="recipe-name explore-btn" id="popular-${recipes[i].idMeal}" href="/view/${recipes[i].idMeal}">Explore</a>
            </div>
          </div>
        </div>
    `);
  }
}

function findIdMealByName(meals, mealName) {
  for (let i = 0; i < meals.length; i++) {
    if (meals[i].mealName === mealName) {
      return meals[i].idMeal;
    }
  }
  // If no matching meal is found, return null or handle the case as needed
  return null;
}

function addFields(clone, formGroup) {
  // Clone the ingredients-measures div
  var newIngredientMeasure = $(clone).first().clone();

  // Clear input values in the cloned element
  newIngredientMeasure.find('input[type="text"]').val("");

  // Append the cloned element to the form group
  $(formGroup).append(newIngredientMeasure);
}

function removeFields(elementToBeRemoved, e) {
  // if only one elementToBeRemoved, don't do anything
  var ingredientMeasuresCount = $(elementToBeRemoved).length;
  if (ingredientMeasuresCount > 1) {
    var parentElement = $(e.target).closest(elementToBeRemoved);

    // Remove the specific parent element
    parentElement.remove();
  }
}

function serializeFormData() {
  return $("form")
    .serializeArray()
    .reduce(function (obj, item) {
      if (item.name === "category") {
        obj[item.name] = item.value.split(",").map(function (category) {
          return category.trim();
        });
      } else if (item.name === "nutrition") {
        obj["nutritionFacts"] = {};

        // Get all .nutrition-facts elements
        $(".nutrition-facts").each(function () {
          var nutritionName = $(this).find("#nutrition").val();
          var nutritionAmount = $(this).find("#amount").val();
          obj["nutritionFacts"][nutritionName] = nutritionAmount;
        });
      } else if (item.name === "ingredients") {
        obj["ingredientsMeasuers"] = {};

        // Get all .ingredients-measures elements
        $(".ingredients-measures").each(function () {
          var ingredientName = $(this).find("#ingredients").val();
          var ingredientMeasure = $(this).find("#measures").val();
          obj["ingredientsMeasuers"][ingredientName] = ingredientMeasure;
        });
      } else {
        // Exclude "amount" and "measures" fields
        if (item.name != "amount" && item.name != "measures")
          obj[item.name] = item.value;
      }
      return obj;
    }, {});
}

function addLayer(targetEle, className) {
  var content = $(targetEle);
  var beforeElement = $("<div></div>");

  beforeElement.addClass(className);

  content.prepend(beforeElement);
}

function removeLayer(element) {
  $(element).remove();
}

function showMessage(id) {
  addLayer(".content", "content-before");
  addLayer(".nav-con", "nav-con-before");

  $(id).addClass("show");
}

$(document).ready(function () {
  // console.log(meals);

  // set banner images
  $(".bannerImg").each(function (index) {
    $(this).attr("src", popular3Recipes[index].mealThumb);
  });

  displayRecipes(popular3Recipes);

  // autocomplete
  let mealNames = [];

  // meals from server
  meals.forEach((meal) => {
    mealNames.push(meal.mealName);
  });
  $(".search-input-text").autocomplete({
    source: mealNames,
  });

  function showSearchResults() {
    let inputVal = $(".search-input input").val().trim();

    if (inputVal === "") {
      $(".search-input input").val("");
      $(".search-input input").focus();
      return;
    }

    window.location.href = `/search_results/${inputVal}`;
  }

  // show search results
  $(".submit-button").click(function () {
    showSearchResults();
  });

  $(".search-input").on("keyup", function (e) {
    // 13 == "enter"
    if (e.which === 13) {
      showSearchResults();
    }
  });

  // add data
  $(".add-data-button").click(function () {
    window.location.href = `/add`;
  });

  // edit data
  $(".edit-data-btn").click(() => {
    var currentUrl = window.location.href;

    // Split the URL by "/"
    var urlParts = currentUrl.split("/");

    // Extract the part containing "03"
    var lastPart = urlParts[urlParts.length - 1];

    window.location.href = `/edit/${lastPart}`;
  });

  // filter
  $(".cal-plus-btn").click(() => {
    $(".cal-level-option-con").toggleClass("show");
  });

  $(".type-plus-btn").click(() => {
    $(".type-option-con").toggleClass("show");
  });

  $(".area-plus-btn").click(() => {
    $(".area-option-con").toggleClass("show");
  });

  // filter by
  $("#filter-btn").click(() => {
    // Array to store checked values
    var checkedValues = [];

    $(".cal-level-checkbox:checked").each(function () {
      checkedValues.push($(this).val());
    });

    $(".type-option-checkbox:checked").each(function () {
      checkedValues.push($(this).val());
    });

    $(".area-option-checkbox:checked").each(function () {
      checkedValues.push($(this).val());
    });

    if (checkedValues.length === 0) return;

    $.ajax({
      type: "POST",
      url: "/filter_by",
      data: JSON.stringify(checkedValues),
      contentType: "application/json",
      success: function (response) {
        // Handle success response

        let idMeals = response.filtered_meals.map((meal) => meal.idMeal);

        let idStrings = idMeals.map((id) => `${id}`).join(",");
        let checkedValStrings = response.checked_values
          .map((value) => `${encodeURIComponent(value)}`)
          .join(",");

        window.location.href = `/display_filter_results?ids=${idStrings}&checkedVals=${checkedValStrings}`;
      },
      error: function (error) {
        // Handle error response
        console.error("Error:", error);
      },
    });
  });
});
