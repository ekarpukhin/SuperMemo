export function getModalHtml(str_out_text){
    var str_html = `<div class="modal fade" id="CardModal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header bg-light">
          <h5 class="modal-title">Напиши перевод слова</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <form id="input-form">
        <div class="modal-body">
          <p>` + str_out_text + `</p>
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
  return str_html;
}