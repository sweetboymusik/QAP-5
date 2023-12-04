// Reading JSON Data Using fetch()
// Date Written: December 04, 2023
// Author: Elliott Butt

console.log("Meet My Cats:");

fetch("./cat_data.json")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((cat) => {
      let pronoun = "";
      cat.gender === "male" ? (pronoun = "He") : (pronoun = "She");

      console.log(
        `${cat.name} (AKA ${cat.nicknames[0]}) is a ${cat.age} year old ${cat.color} ${cat.breed}. ${pronoun} is a cutie! You can usually find them ${cat.favs.activity}, or sleeping ${cat.favs.sleepLocation}.`
      );
    });
  })
  .catch((error) => {
    console.log(`Error details: ${error}`);
  });
