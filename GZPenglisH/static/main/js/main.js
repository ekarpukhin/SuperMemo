function getAnswer(){
  let form = document.getElementById("input-form");

  function complete(value) {
    document.onkeydown = null;
    window.alert( value );
  }

  form.onsubmit = function (){
    let value = form.text.value;
    if (value == '') return false;

    complete(value);
  };

  return form.text.value;
}


let modalWrap = null;

const showModal = arguments => {
  if (modalWrap !== null) {
    modalWrap.remove();
  }

  let str_out = arguments;
  if (typeof arguments !== "string") {
    str_out = arguments[0]
  }
  let str_in = null;

  modalWrap = document.createElement('div');
  modalWrap.innerHTML = `
    <div class="modal fade" id="CardModal">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header bg-light">
            <h5 class="modal-title">Напиши перевод</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <form id="input-form">
          <div class="modal-body">
            <p>` + arguments + `</p>
           <input name="text" type="text" size="50">
          </div>
          <div class="modal-footer justify-content-center">
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Закончить!</button>
            <input type="submit" class="btn btn-success modal-success-btn" value="Ответить!">
          </div>
          </form>
        </div>
      </div>
    </div>
  `;


  modalWrap.querySelector('.modal-success-btn').onclick = function (){
    str_in = getAnswer();
//"/courses/views/urls/get_answer_from_js",
    $.ajax({
    url: "/courses/templates/courses/someshit.py",
    type: "POST",
    dataType: "json",
    data: {
      url: str_in,
      csrfmiddlewaretoken: '{{ csrf_token }}'
    },
    error: function (xhr, errmsg, err) {
      window.alert("Sending to Django: something went wrong!\n" + xhr.status + ": " + xhr.responseText);
    }
  });
  };

  document.body.append(modalWrap);

  let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
  modal.show();
}


