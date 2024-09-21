$(document).ready(function () {
  displayRecipes(search_results, input);

  let htmlContent =
    search_results.length !== 0
      ? `
    <h3> Showing ${search_results.length} results for <span class="search-input-result">"${input}"</span></h3>`
      : `
   
    <h3>No results found for <span class="search-input-result">"${input}"</span></h3>
    `;

  $(".search-results-title-con").prepend(htmlContent);
});
