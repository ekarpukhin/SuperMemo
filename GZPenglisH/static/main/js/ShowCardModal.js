

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function getAnswer() {
  let form = document.getElementById("input-form");
  let card_modal = document.getElementById("CardModal");
  let text_out = {
      value: form.text.value
  };
  let json_return = null;

  function complete(value) {
      document.onekeydown = null;
      //form.text.value = '';   // Что бы была пустая строка после ввода
  }

  form.onsubmit = function () {
      let value = form.text.value;
      if (value == '') return false;

      $.ajax({
          url: '/courses/get_answer/',
          method: "POST",
          dataType: "json",
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
          },
          data: {
              url: value
          },
      }).done(function (xhr) {
              window.alert("All is good, you're doing fine! status:" + xhr.status+ "\nResponseText\n" + xhr.responseText);
              json_return = xhr;
          }
      ).fail(function (xhr, errmsg, err) {
          //window.alert("Sending to Py: something went wrong!\n" + xhr.status + ": " + xhr.responseText);
      });

      complete(value);
      return false;
  };

  return json_return;
}

let modalWrap = null;


function showModalCard(){
    modalWrap = document.getElementById('OutCardModal');
    modalWrap.querySelector('.modal-success-btn').onclick = function () {
        let str_in = getAnswer();
        window.alert(str_in);
    };

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}