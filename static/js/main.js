//code for printing out recipes
function printRecipe() {
     var print_div = document.getElementById("recipeArea");
     var print_area = window.open();
     print_area.document.write(print_div.innerHTML);
     print_area.document.close();
     print_area.focus();
     print_area.print();
     print_area.close();
}
