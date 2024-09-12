document.getElementById("aiForm").onsubmit = function (event) {
  event.preventDefault();

  var formData = new FormData(this);

  fetch("/ask-ai/", {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("aiResponse").textContent = data.response;
    })
    .catch((error) => {
      document.getElementById("aiResponse").textContent = "An error occurred.";
    });
};
