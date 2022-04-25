var ModalWrap = null;
const showModal = () => {

    if(ModalWrap !== null){
        modalWrap.remove();
    }
    modalWrap = document.createElement("div");
    modalWrap.innerHTML = `
    <div class="modal fade" id="LoginModal" tabindex="-1" aria-labelledby="LoginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Авторизация</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <div class="form">
                <form class="form-horizontal" role="form" method="POST">
                  <div class="form-group">
                    <label for="inputEmail3" class="col-sm-2 control-label">Логин</label>
                    <div class="col-sm-10">
                      <input type="text" id="login_login" class="form-control" placeholder="Логин" name="login_login">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="inputPassword3" class="col-sm-2 control-label">Пароль</label>
                    <div class="col-sm-10">
                      <input type="password" id="password_login" class="form-control" placeholder="Пароль" name="password_login">
                    </div>
                  </div> 
                </form>
            </div>
            <div class="result" id="errorMessage_login"></div>
        </div>
        <div class="modal-footer justify-content-center">
          <button type="button" class="btn btn-success" id="Login-button" name="login-button">Log In</button>
        </div>
      </div>
    </div>
    </div>
    `;

    document.body.append(ModalWrap);
    var modal = new BootstrapModal.Modal(ModalWrap.querySelector('.modal'));
    modal.show();
}