$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();

	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;
			});
		} else{
			checkbox.each(function(){
				this.checked = false;
			});
		}
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

/*----------------
|   sweetalert   |
----------------*/

function SwalValidation(Errormsg) {
    var msgHtmlmessage = "";

    Errormsg.forEach(function (message) {
		msgHtmlmessage += "<div class='alert_css'><i class='fa fa-exclamation-triangle ' aria-hidden='true'></i>" + message + "</div>";
	});

    swal({
        title: 'Validation Error',
        text: "",
        html: msgHtmlmessage,
        type: "error",
        showCancelButton: false,
        confirmButtonClass: 'btn-danger',
        confirmButtonText: 'Ok!',
        focusConfirm: true
    });
}

function SwalSuccessFocus(msg, elementfocus) {
    debugger;
    swal({
        type: "success",
        title: "Success",
        text: msg,
        timer: 4000,
        onAfterClose: () => {
            setTimeout(() => $('#' + elementfocus).focus(), 110);
        }
    })    
}

function SwalSuccess(msg) {
    debugger;
    // swal({
    //     type: "success",
    //     title: "Success",
    //     text: msg,
    //     timer: 4000
    // })
    swal({
        title: "Success !",
        text: msg,
        icon: "success",
        buttons: true, //"OK",
        //dangerMode: true,
        timer: 4000,
    });
}

function SwalWarning(msg) {
    swal({
        // type: 'warning',
        title: 'Warning !',
        text: msg,
        icon: 'warning',
        timer: 5000
    });
}

function SwalError(msg) {
    swal({
        // type: 'error',
        title: 'Error !',
        text: msg,
        icon: 'error',
        // buttons: true, //"OK",
    });
}

function SwalInfo(msg) {
    swal({
        // type: 'error',
        title: 'Info !',
        text: msg,
        icon: 'info',
        // buttons: true, //"OK",
    });
}
