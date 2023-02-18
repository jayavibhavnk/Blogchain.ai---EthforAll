import { blogArray } from "./blogs.js";
console.log("from the blogs.js", blogArray);

let x = 1;
for (let blog in blogArray) {
  document.getElementById(`titlespace${x}`).innerHTML = blogArray[blog].title;
  document.getElementById(`imgspace${x}`).src = blogArray[blog].image0;
  document.getElementById(`category${x}`).innerHTML = blogArray[blog].category;
  document.getElementById(`content${x}`).innerHTML =
    blogArray[blog].blog_content.substring(0, 100) + "...";
  document.getElementById(`authorspace${x}`).innerHTML =
    "by " + blogArray[blog].author;

  x++;
}
