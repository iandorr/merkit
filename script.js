// Smooth scrolling for browsers that don't support CSS smooth scrolling
if (
  window.getComputedStyle(document.documentElement).scrollBehavior !== "smooth"
) {
  document.querySelectorAll('a[href^="#"]').forEach((internalLink) => {
    const targetElement = document.querySelector(
      internalLink.getAttribute("href")
    );
    if (targetElement) {
      internalLink.addEventListener("click", (e) => {
        targetElement.scrollIntoView({
          behavior: "smooth",
        });
        e.preventDefault();
      });
    }
  });
}

const root = document.querySelector(":root");

const email = document.getElementById("mail");
const emailError = document.querySelector("#mail ~ span.error");
const firstname = document.getElementById("first-name");
const firstnameError = document.querySelector("#first-name ~ span.error");
const lastname = document.getElementById("last-name");
const lastnameError = document.querySelector("#last-name ~ span.error");
const countrycode = document.getElementById("countrycode");
const countrycodeError = document.getElementById("countrycode-error");
const phone = document.getElementById("phone-number");
const phoneError = document.getElementById("phone-number-error");
const subject = document.getElementById("subject");
const subjectError = document.querySelector("#subject ~ span.error");
const message = document.getElementById("message");
const messageError = document.querySelector("#message ~ span.error");
const emailInvalid = document.querySelectorAll("#mail ~ .invalid-feedback");

(function () {
  "use strict";
  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "input",
      function (event) {
        if (email.validity.valid) {
          emailError.innerHTML = "";
          email.classList.add("was-validated");
        } else {
          showError("email");
        }

        if (firstname.validity.valid) {
          firstnameError.innerHTML = "";
        } else {
          showError("first-name");
        }

        if (lastname.validity.valid) {
          lastnameError.innerHTML = "";
        } else {
          showError("last-name");
        }

        if (countrycode.validity.valid) {
          countrycodeError.innerHTML = "";
        } else {
          showError("countrycode");
        }

        if (phone.validity.valid) {
          phoneError.innerHTML = "";
        } else {
          showError("phone-number");
        }

        if (subject.validity.valid) {
          subject.innerHTML = "";
        } else {
          showError("subject");
        }

        if (message.validity.valid) {
          messageError.innerHTML = "";
        } else {
          showError("message");
        }

        form.addEventListener("submit", function (event) {
          if (!email.validity.valid) {
            showError("email");
            event.preventDefault();
          } else if (!firstname.validity.valid) {
            showError("first-name");
            event.preventDefault();
          } else if (!lastname.validity.valid) {
            showError("last-name");
            event.preventDefault();
          } else if (!countrycode.validity.valid) {
            showError("countrycode");
            event.preventDefault();
          } else if (!phone.validity.valid) {
            showError("phone-number");
            event.preventDefault();
          } else if (!subject.validity.valid) {
            showError("subject");
            event.preventDefault();
          } else if (!message.validity.valid) {
            showError("message");
            event.preventDefault();
          }
          form.classList.add("was-validated");
        });

        function showError(input) {
          if (input == "email") {
            if (email.validity.valueMissing) {
              emailError.innerHTML = "Prosím, zadejte e-mailovou adresu.";
            }
            if (email.validity.typeMismatch) {
              emailError.innerHTML = "Akceptovaný formát: jmeno@domena";
            }
            if (email.validity.tooShort) {
              emailError.innerHTML = `Minimální délka e-mailu je ${email.minLength} znaků.`;
            }
            emailError.className = "invalid-feedback";
          }
          if (input == "first-name") {
            if (firstname.validity.valueMissing) {
              firstnameError.innerHTML = "Prosím, zadejte jméno.";
            }
            if (firstname.validity.patternMismatch) {
              firstnameError.innerHTML = "Jméno může obsahovat pouze písmena.";
            }
            if (firstname.validity.tooShort) {
              firstnameError.innerHTML = `Minimální délka jména je ${firstname.minLength} znaků.`;
            }
            firstnameError.className = "invalid-feedback";
          }
          if (input == "last-name") {
            if (lastname.validity.valueMissing) {
              lastnameError.innerHTML = "Prosím, zadejte příjmení.";
            }
            if (lastname.validity.patternMismatch) {
              lastnameError.innerHTML =
                "Příjmení může obsahovat pouze písmena.";
            }
            if (lastname.validity.tooShort) {
              lastnameError.innerHTML = `Minimální délka příjmení je ${lastname.minLength} znaků.`;
            }
            lastnameError.className = "invalid-feedback";
          }
          if (input == "countrycode") {
            if (countrycode.validity.valueMissing) {
              countrycodeError.innerHTML = "Prosím, zadejte předvolbu.";
            }
            if (countrycode.validity.patternMismatch) {
              countrycodeError.innerHTML = "Prosím, zadejte platnou předvolbu.";
            }
            if (countrycode.validity.tooShort) {
              countrycodeError.innerHTML = `Minimální délka předvolby je ${countrycode.minLength} znaků.`;
            }
            countrycodeError.className = "invalid-feedback";
          }
          if (input == "phone-number") {
            if (phone.validity.valueMissing) {
              phoneError.innerHTML = "Prosím, zadejte telefonní číslo.";
            }
            if (phone.validity.patternMismatch) {
              phoneError.innerHTML =
                "Telefonní číslo může obsahovat pouze číslice (0-9).";
            }
            if (phone.validity.tooShort) {
              phoneError.innerHTML = `Minimální délka telefonního čísla je ${phone.minLength} znaků.`;
            }
            phoneError.className = "invalid-feedback";
          }
          if (input == "subject") {
            if (subject.validity.valueMissing) {
              subjectError.innerHTML = "Prosím, zadejte pŕedmět.";
            }
            if (subject.validity.typeMismatch) {
              subjectError.innerHTML =
                "Předmět může obsahovat jakékoliv znaky.";
            }
            if (subject.validity.tooShort) {
              subjectError.innerHTML = `Minimální délka předmětu je ${subject.minLength} znaků.`;
            }
            subjectError.className = "invalid-feedback";
          }
          if (input == "message") {
            if (message.validity.valueMissing) {
              messageError.innerHTML = "Prosím, zadejte tělo zprávy.";
            }
            if (message.validity.typeMismatch) {
              messageError.innerHTML = "Zpráva může obdahovat jakékoliv znaky.";
            }
            if (message.validity.tooShort) {
              messageError.innerHTML = `Minimální délka zprávy je ${message.minLength} znaků.`;
            }
            messageError.className = "invalid-feedback";
          }
        }

        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        event.preventDefault();
      },
      false
    );
  });
})();

// aby po submite zostal vo view form
window.addEventListener("load", function () {
  // Change scroll behavior
  root.setAttribute("style", "scroll-behavior: auto;");

  // Timeout ensures styles are applied before scrolling
  setTimeout(function () {
    // Reset to CSS defaults.
    root.removeAttribute("style");
  }, 2);
});














// Navigation - mobile nav toggle

const primNav = document.querySelector('.primary-nav');
const primNavToggle = document.querySelector('.primary-nav__mobile-toggle');

primNavToggle.addEventListener('click', () => {
  const visible = primNav.getAttribute('data-visible');

  if (visible === 'false') {
    primNav.setAttribute('data-visible', true);
    primNavToggle.setAttribute('aria-expanded', true);
  } else if (visible === 'true') {
    primNav.setAttribute('data-visible', false);
    primNavToggle.setAttribute('aria-expanded', false);
  }
})

// Navigation - hide mobile navigation when nav link is clicked

const primNavLinks = document.querySelectorAll('.primary-nav__link');

for (let c = 0; c < primNavLinks.length; c++) {
  primNavLinks[c].addEventListener('click', () => {
    primNav.setAttribute('data-visible', false);
    primNavToggle.setAttribute('aria-expanded', false);
  })
}

// Navigation - active class based on scroll / click in the menu
const navPoints = document.querySelectorAll('.js-active-on-scroll')
const navLinks = document.querySelectorAll('.primary-nav__link')
let prevScrollpos = window.pageYOffset


window.onscroll = () => {
  let currentScroll = ''

  let currentScrollPos = window.pageYOffset
  let header = document.getElementById('primary-header')
  if (prevScrollpos > currentScrollPos) {
    header.style.top = "0"
  } else {
    let headerHight = '-' + header.offsetHeight + 'px'
    header.style.top = headerHight
  }
  prevScrollpos = currentScrollPos

  navPoints.forEach( section => {
    const sectionTop = section.offsetTop
    // console.log(section)
    if (scrollY >= sectionTop - 5) {
      currentScroll = section.getAttribute('id')
    }
  })

  navLinks.forEach( link => {
    link.classList.remove('active')
    if (link.classList.contains(currentScroll)) {
      link.classList.add('active')
    }
  })
}

// Navigation - hide on scrolldown, show on scrollup
// let prevScrollpos = window.pageYOffset
// window.onscroll = function() {
//   let currentScrollPos = window.pageYOffset
//   let header = document.getElementById('primary-header')
//   if (prevScrollpos > currentScrollPos) {
//     header.style.top = "0"
//   } else {
//     let headerHight = '-' + header.offsetHeight + 'px'
//     header.style.top = headerHight
//   }
//   prevScrollpos = currentScrollPos
// }

// DEBUG - DOESNT WORK WITH THE ACTIVE SCROLL

// Hero video playback speed
document.getElementById('hero-video').playbackRate = .7;