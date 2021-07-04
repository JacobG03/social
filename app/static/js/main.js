// Get default user data
const getData = async () => {
    let users = []
    try {
        const response = await fetch('http://127.0.0.1:5000/api/users')
        const data = await response.json()
        users = data

        // Call function to render users inside
        renderUsers(users);

    } catch (error) {
        console.log(error)
    }
}


getData();


// Display users
function renderUsers (users) {
    console.log(users)
}



// Functions for display and hiding the user page
// Has to be window.onload or will return elements as null

// TODO
// Closes when users clicks another user
// Closes when user clicks X
//! Option on the user page to click next or last
//!   and the last/next user page will be displayed
//* Add transitions


// Variable holding the current state of some 'user-page'
var state = {
    'displayed': false,
    'current' : ''    // 'user-5', 'user-76'
}

var displayUserPage = function (user_id) {
    var userpage = 'userpage-' + user_id;
    console.log(userpage);
    var userpage_element = document.getElementById('userpage-1');
    userpage_element.classList.toggle('display-block');
}

window.onload = function() {
    var users = document.getElementsByClassName('user')
    console.log(users)
    for (let i = 0; i < users.length; i++) {
        var id = users[i].id.split('-')[1]
        console.log(id)
        users[i].addEventListener('click', displayUserPage.bind(event, id), false)
    }
}
