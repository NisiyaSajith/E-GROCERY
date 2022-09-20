// form validate
const forms=Array.from(document.getElementsByTagName("form"));



if (forms) {
  forms.map((form) => {
        let elements = Array.from(form);
        elements.map((elem)  => {
            if (elem.tagName.toLowerCase() == "input") {
                elem.classList.add("form-control");
            }else if(elem.tagName.toLowerCase() == "label") {
                elem.classList.add("form-label");
            }else if(elem.tagName.toLowerCase() == "textarea") {
                elem.classList.add("form-control");
            }
            
        
        });
    });
};


  //Show the hidden html elements
  cardImgs.forEach((cardImg) => {
    cardImg.style.visibility = "visible";
  });
  cardTitleSpans.forEach((cardTitleSpan) => {
    cardTitleSpan.style.visibility = "visible";
  });
  cardDescSpans.forEach((cardDescSpan) => {
    cardDescSpan.style.visibility = "visible";
  });

