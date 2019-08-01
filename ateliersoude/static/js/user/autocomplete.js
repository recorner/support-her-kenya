let inputEmailSelector = 'input[name="email"]';
let inputMainFieldSelector = 'input[name="main_field"]';
var inputs;
var choices;
if (document.querySelectorAll(inputMainFieldSelector).length == 0){
    inputs = document.querySelectorAll(inputEmailSelector)
} else {
    inputs = document.querySelectorAll(inputMainFieldSelector)
}
inputs.forEach(function (node) {
    new autoComplete({
        selector: node,
        minChars: 3,
        source: function(user, suggest){
            let term = user.toLowerCase();
            let choices = JSON.parse(document.getElementById('users-data').textContent);
            let matches = [];
            for (let i=0; i<choices.length; i++) {
                let searchableString = (document.querySelectorAll(inputEmailSelector).length == 0) ? choices[i].toLowerCase() : choices[i][0].toLowerCase();
                if (searchableString.includes(term)) {
                    matches.push(choices[i]);
                }
            }
            suggest(matches);
        },
        renderItem: function (item, search){
            console.log(item);
            if (document.querySelectorAll(inputEmailSelector).length == 0) {
                return '<div class="autocomplete-suggestion" data-val="' + item + '">' + item +'</div>';
            } else {
                search = search.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
                let re = new RegExp("(" + search.split(' ').join('|') + ")", "gi");
                return '<div class="autocomplete-suggestion" data-val="' + item[1] + '">' + item[0].replace(re, "<b>$1</b>") + '</div>';
            }
        },
    });
});
