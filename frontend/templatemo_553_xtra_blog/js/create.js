"use strict";

let idNumber = 1;
document.getElementById("myform").addEventListener("submit", function (event) {
  event.preventDefault();
  let formData = {};
  //   formData.id = document.getElementById("id").value;
  formData.id = idNumber;
  idNumber++;
  formData.title = document.getElementById("title").value;
  formData.blog_content = document.getElementById("blog_content").value;
  formData.author = document.getElementById("author").value;
  formData.category = document.getElementById("category").value;

  let jsonFile = formData;
  console.log(jsonFile);

  //   posting the json file to api
  // fetch("http://127.0.0.1:8000/blog", {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  //   body: jsonFile,
  // })
  //   .then((response) => {
  //     if (response.ok) {
  //       console.log("post successful");
  //       return response.json();
  //     } else {
  //       throw new Error("Network response was not ok");
  //     }
  //   })
  //   .then((data) => {
  //     console.log(data);
  //   })
  //   .catch((error) => {
  //     console.error("There was a problem with the fetch operation:", error);
  //   });

  async function api() {
    console.log(jsonFile);
    const response = await fetch("http://127.0.0.1:5000/blog", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(jsonFile),
    })
      .then((response) => response.json())
      .then((response) => console.log(JSON.stringify(response)));
  }

  api();
});
