function handleAjaxResponse(response, redirectLocation) {
  // Handle the success response here

  $(
    "input[type='text'], input[type='number'], input[type='url'], textarea"
  ).val("");

  showMessage("#successMessage");

  $("#seeItemBtn").click(function () {
    removeLayer(".content-before");
    removeLayer(".nav-con-before");
    window.location.href = `/view/${response.idMeal}`;
  });

  $("#addNewItemBtn").click(function () {
    removeLayer(".content-before");
    removeLayer(".nav-con-before");
    // window.location.href = "/add";
    window.location.href = redirectLocation;
  });
}

$(document).ready(function () {
  $("#mealName").focus();

  $("form").submit(function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    var action = $(this).attr("action");
    if (action === "/add") {
      // Serialize form data into a JSON object
      var formData = serializeFormData();

      $.ajax({
        type: "POST",
        url: "/add",
        data: JSON.stringify(formData),
        contentType: "application/json",
        success: function (response) {
          // if add route
          handleAjaxResponse(response, "/add");
        },
        error: function (error) {
          // Handle the error response here
          console.error(error);
        },
      });
    }
  });

  $(document).on("click", ".add-ingredient", function () {
    addFields(".ingredients-measures", ".ing-measures-con");
  });

  $(document).on("click", ".add-nutrition", function () {
    addFields(".nutrition-facts", ".nutrition-facts-con");
  });

  $(document).on("click", ".remove-ingredient", function (e) {
    removeFields(".ingredients-measures", e);
  });

  $(document).on("click", ".remove-nutrition", function (e) {
    removeFields(".nutrition-facts", e);
  });
});
