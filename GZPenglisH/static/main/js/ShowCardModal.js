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

  function complete(value) {
      document.onekeydown = null;
      //form.text.value = '';
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
              //window.alert("All is good, you're doing fine! status:" + xhr.status+ "\nResponseText\n" + xhr.responseText);
              if (xhr.answer_status == true){
                card_modal.classList.add("correct_animation");
              }
          }
      ).fail(function (xhr, errmsg, err) {
          //window.alert("Sending to PHP: something went wrong!\n" + xhr.status + ": " + xhr.responseText);
      });

      complete(value);
      return false;
  };

  return text_out.value;
}


let modalWrap = null;

function showModalCard(data){
    if (modalWrap !== null) {
        modalWrap.remove();
    }

    let str_out = data;
    let str_in = null;
    if (typeof data !== "string") {
        str_out = data[0]
    }


    modalWrap = document.createElement('div');
    modalWrap.innerHTML = `<div class="modal fade" id="CardModal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header bg-light">
          <h5 class="modal-title">Напиши перевод слова</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <form id="input-form">
        <div class="modal-body">
          <p>` + str_out + `</p>
          <input name="text" type="text" size="50">
        </div>
        <div class="modal-footer justify-content-center">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Закончить!</button>
          <input type="submit" class="btn btn-success modal-success-btn" value="Ответить!">
        </div>
        </form>
      </div>
    </div>
  </div>`;

    modalWrap.querySelector('.modal-success-btn').onclick = function () {
        str_in = getAnswer();
        window.alert(str_in);
    };

    document.body.append(modalWrap);

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}