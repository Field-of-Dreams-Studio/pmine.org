const header = document.createElement("div");
header.classList.add("head");
header.style.marginTop = "5%";
header.innerHTML = `<div class="p table table-borderless" style="margin-top: 5%">
        <table align="center" width="90%" style="margin: 0 auto;">
          <tr>
            <td><label for="fulltitle1" style="font-size: 1rem;" class="lang" key="title"></label></td>
            <td><input type="text" id="fulltitle1" name="fulltitle1" data-type="fulltitle" placeholder="" style="font-size: 1rem; width: 100%;"></td>
          </tr>
          <tr>
            <td><label for="tj" style="font-size: 1rem;" class="lang" key="notes"></label></td>
            <td><textarea id="tj" name="tj" data-type="tj" placeholder="" rows="10" cols="50" style="font-size: 1rem; width: 100%;"></textarea></td>
          </tr>
        </table>
      </div> `

const body = document.createElement("div");
body.classList.add("para");
body.classList.add("sub");
body.style.marginTop = "5%"; 
body.innerHTML = `<div class="p table table-borderless" style="margin-top: 5%">
        <table align="center" width="90%" style="margin: 0 auto;"> 
          <tr>
            <td><label for="fulltitle1" style="font-size: 1rem;" class="lang" key="title"></label></td>
            <td><input type="text" id="fulltitle1" name="fulltitle1" data-type="fulltitle" placeholder="" style="font-size: 1rem; width: 100%;"></td>
          </tr> 
          <tr>
            <td><label for="honmo" style="font-size: 1rem;" class="lang" key="honmo"></label></td>
            <td><textarea id="honmo" name="honmo" data-type="honmo" placeholder="" rows="10" cols="50" style="font-size: 1rem; width: 100%;"></textarea></td>
          </tr>
        </table>
      </div> ` 

function getheader() {
  return header
}

function getbody() {
  return body
}
