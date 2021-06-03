const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const reportForm = document.getElementById('report-form')
const alertBox = document.getElementById('alert-box')

const reportName = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value



const handleAlert = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}


// if (img) {
//     reportBtn.classList.remove('not-visible')
// }

reportBtn.addEventListener('click', ()=>{

    // console.log(img.src)

    reportForm.addEventListener('submit', e=>{
        e.preventDefault()
        const formData = new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('name', reportName.value)
        formData.append('remarks', reportRemarks.value)
        formData.append('image', img.src)

        $.ajax({
            type: 'POST',
            url: '/reports/save/',
            data: formData,
            success: function(response) {
                console.log(response)
                handleAlert('success', 'Report Created Succesfully.')
                reportForm.reset()
            },
            error: function(error) {
                console.log(error)
                handleAlert('danger', 'Something went wrong!')
            },
            processData: false,
            contentType: false,
        })
    })
})