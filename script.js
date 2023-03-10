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
              emailError.innerHTML = "Pros??m, zadejte e-mailovou adresu.";
            }
            if (email.validity.typeMismatch) {
              emailError.innerHTML = "Akceptovan?? form??t: jmeno@domena";
            }
            if (email.validity.tooShort) {
              emailError.innerHTML = `Minim??ln?? d??lka e-mailu je ${email.minLength} znak??.`;
            }
            emailError.className = "invalid-feedback";
          }
          if (input == "first-name") {
            if (firstname.validity.valueMissing) {
              firstnameError.innerHTML = "Pros??m, zadejte jm??no.";
            }
            if (firstname.validity.patternMismatch) {
              firstnameError.innerHTML = "Jm??no m????e obsahovat pouze p??smena.";
            }
            if (firstname.validity.tooShort) {
              firstnameError.innerHTML = `Minim??ln?? d??lka jm??na je ${firstname.minLength} znak??.`;
            }
            firstnameError.className = "invalid-feedback";
          }
          if (input == "last-name") {
            if (lastname.validity.valueMissing) {
              lastnameError.innerHTML = "Pros??m, zadejte p????jmen??.";
            }
            if (lastname.validity.patternMismatch) {
              lastnameError.innerHTML =
                "P????jmen?? m????e obsahovat pouze p??smena.";
            }
            if (lastname.validity.tooShort) {
              lastnameError.innerHTML = `Minim??ln?? d??lka p????jmen?? je ${lastname.minLength} znak??.`;
            }
            lastnameError.className = "invalid-feedback";
          }
          if (input == "countrycode") {
            if (countrycode.validity.valueMissing) {
              countrycodeError.innerHTML = "Pros??m, zadejte p??edvolbu.";
            }
            if (countrycode.validity.patternMismatch) {
              countrycodeError.innerHTML = "Pros??m, zadejte platnou p??edvolbu.";
            }
            if (countrycode.validity.tooShort) {
              countrycodeError.innerHTML = `Minim??ln?? d??lka p??edvolby je ${countrycode.minLength} znak??.`;
            }
            countrycodeError.className = "invalid-feedback";
          }
          if (input == "phone-number") {
            if (phone.validity.valueMissing) {
              phoneError.innerHTML = "Pros??m, zadejte telefonn?? ????slo.";
            }
            if (phone.validity.patternMismatch) {
              phoneError.innerHTML =
                "Telefonn?? ????slo m????e obsahovat pouze ????slice (0-9).";
            }
            if (phone.validity.tooShort) {
              phoneError.innerHTML = `Minim??ln?? d??lka telefonn??ho ????sla je ${phone.minLength} znak??.`;
            }
            phoneError.className = "invalid-feedback";
          }
          if (input == "subject") {
            if (subject.validity.valueMissing) {
              subjectError.innerHTML = "Pros??m, zadejte p??edm??t.";
            }
            if (subject.validity.typeMismatch) {
              subjectError.innerHTML =
                "P??edm??t m????e obsahovat jak??koliv znaky.";
            }
            if (subject.validity.tooShort) {
              subjectError.innerHTML = `Minim??ln?? d??lka p??edm??tu je ${subject.minLength} znak??.`;
            }
            subjectError.className = "invalid-feedback";
          }
          if (input == "message") {
            if (message.validity.valueMissing) {
              messageError.innerHTML = "Pros??m, zadejte t??lo zpr??vy.";
            }
            if (message.validity.typeMismatch) {
              messageError.innerHTML = "Zpr??va m????e obdahovat jak??koliv znaky.";
            }
            if (message.validity.tooShort) {
              messageError.innerHTML = `Minim??ln?? d??lka zpr??vy je ${message.minLength} znak??.`;
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


let prevScrollPos = 0;
window.onscroll = () => {
  let currentScroll = ''

  let currentScrollPos = window.pageYOffset
  let header = document.getElementById('primary-header')
  if (prevScrollPos > currentScrollPos) {
    header.style.top = "0"
  } else {
    let headerHight = '-' + header.offsetHeight + 'px'
    header.style.top = headerHight
  }
  prevScrollPos = currentScrollPos

  if (prevScrollPos > currentScrollPos) {
    currentScroll = ""
  }

  navPoints.forEach( section => {
    const sectionTop = section.offsetTop
    if (currentScrollPos >= sectionTop + 800) {
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
const herVideo = document.getElementById('hero-video')
if (herVideo) {
  herVideo.playbackRate = .7
}