function toggle(header, div_id) {
    let div = document.getElementById(div_id)
    header.textContent = (div.style.display === 'none') ? 'Hide' : 'Leave message'
    div.style.display = (div.style.display === 'none') ? 'block' : 'none'
}

function fill_reply_id(field_id, reply_id){
    document.getElementById(field_id).value = reply_id
    document.getElementById('reply_label').textContent = '| replying to message #' + reply_id
}

function clear_reply_id(field_id){
    document.getElementById(field_id).value = undefined
    document.getElementById('reply_label').textContent = ''
}