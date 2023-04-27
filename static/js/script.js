
let title = document.querySelector('[name="title"]').value
let content = document.querySelector('[name="content"]').value
let author = parseInt(document.querySelector('[name="author"]').value)




async function destroyPost(post_id){
    data = {
        method: 'DELETE',
        headers:{
            'Content-type': 'application/text'
        }
    }
    try{
        const res = await fetch(`/api/post/delete/${post_id}/`,data)
        
    }catch(err){
        console.log('Error:', err)
    }
    

}
 

async function fetchPostsList(){

    // cleare all html tags
    document.querySelector('.row').innerHTML =''

    try{  
        const res = await fetch('/api/post/list/')
        const posts = await res.json()
        displayPosts(posts)
    }
    catch(err){
        console.log('Error with fetch: ',err)
    }

    
}


document.querySelector('.row').addEventListener('click', (e)=>{
    if(e.target.getAttribute('id') == 'full-post'){
        const url = e.target.getAttribute('data-id')    
        postDetail(url)

        
    }

})


function createPost(post){
    document.querySelector('.row').innerHTML = `
    <div class="col-md-8">
    <div class="media g-mb-30 media-comment">
    <img class="d-flex g-width-50 g-height-50 rounded-circle
        g-mt-3 g-mr-15"
        src="https://bootdey.com/img/Content/avatar/avatar7.png"
        alt="Image Description">
    <div class="media-body u-shadow-v18 g-bg-secondary
        g-pa-30">
        <div class="g-mb-15">
            <h4 class="h5 g-color-gray-dark-v1 mb-0">Published by: ${post.author}</h4>
            <h5 class="g-color-gray-dark-v1 mb-0">Title: ${post.title}</h5>
            <span class="g-color-gray-dark-v4
                g-font-size-12"><small><u>Published:</u> ${new Date(post.publish_date).toUTCString()}</small></span><br>
            
            <span class="g-color-gray-dark-v4
                g-font-size-12"><small><u>Last Updated:</u> ${new Date(post.last_updated).toUTCString()}</small></span>
        </div>
        <p>${post.content}</p>
        <ul class="list-inline d-sm-flex my-0">
            <li class="list-inline-item g-mr-20">
                <a class="u-link-v5 g-color-gray-dark-v4
                    g-color-primary--hover" >
                    <i class="fa fa-thumbs-up g-pos-rel
                        g-top-1 g-mr-3"></i>
                    178
                </a>
            </li>
            <li class="list-inline-item g-mr-20">
                <a class="u-link-v5 g-color-gray-dark-v4
                    g-color-primary--hover" >
                    <i class="fa fa-thumbs-down g-pos-rel
                        g-top-1 g-mr-3"></i>
                    34
                </a>
            </li>
            <li class="list-inline-item ml-auto">
                <a class="u-link-v5 g-color-gray-dark-v4
                    g-color-primary--hover" >
                    <i class="fa fa-reply g-pos-rel g-top-1
                        g-mr-3"></i>
                    Reply
                </a>
            </li>
            <li class="list-inline-item ml-auto">
            <a id="full-post" class="u-link-v5 g-color-gray-dark-v4
                g-color-primary--hover" data-id="" href="/api/post/home/">
                <i class="fa fa-reply g-pos-rel g-top-1
                    g-mr-3"></i>
                Full-List 
            </a>
        </li>
        </ul>
        </div>
        </div>
    </div>
        `

}

async function postDetail(url){

            // retrieve the new post
            const res = await fetch(url)
            const post = await res.json()

    console.log('post: ', post )

            // Populate the fields to get update
            document.querySelector('[name="title"]').value = post.title
            document.querySelector('[name="content"]').value = post.content
            document.querySelector('[name="author"]').value = post.author
            document.querySelector('[type="submit"]').value = 'Update'
            post_id = post.id.split('/')
            post_id = post_id[post_id.length -2]      
            document.querySelector('[type="submit"]').setAttribute('post-id', post_id)

            // show a single post
            createPost(post)


}


function displayPosts(posts){
    posts.forEach((post) => {
        post_id = post.id.split('/')
        post_id = post_id[post_id.length -2]   

        let div = document.createElement('div')
        div.classList.add('col-md-8')

        div.innerHTML = `
        <div class="media g-mb-30 media-comment">
        <img class="d-flex g-width-50 g-height-50 rounded-circle
            g-mt-3 g-mr-15"
            src="https://bootdey.com/img/Content/avatar/avatar7.png"
            alt="Image Description">
        <div class="media-body u-shadow-v18 g-bg-secondary
            g-pa-30">
            <div class="g-mb-15">
                <h5 class="h5 g-color-gray-dark-v1 mb-0">Published by: ${post.author}</h5>
                <span class="g-color-gray-dark-v4
                    g-font-size-12"><small><u>Published:</u> ${new Date(post.publish_date).toUTCString()}</small></span><br>
                
                <span class="g-color-gray-dark-v4
                    g-font-size-12"><small><u>Last Updated:</u> ${new Date(post.last_updated).toUTCString()}</small></span>
            </div>
            <p>${post.content}</p>
            <ul class="list-inline d-sm-flex my-0">
                <li class="list-inline-item g-mr-20">
                    <a class="u-link-v5 g-color-gray-dark-v4
                        g-color-primary--hover" >
                        <i class="fa fa-thumbs-up g-pos-rel
                            g-top-1 g-mr-3"></i>
                        178
                    </a>
                </li>
                <li class="list-inline-item g-mr-20">
                    <a class="u-link-v5 g-color-gray-dark-v4
                        g-color-primary--hover" >
                        <i class="fa fa-thumbs-down g-pos-rel
                            g-top-1 g-mr-3"></i>
                        34
                    </a>
                </li>
                <li class="list-inline-item ml-auto">
                    <a class="u-link-v5 g-color-gray-dark-v4
                        g-color-primary--hover" >
                        <i class="fa fa-reply g-pos-rel g-top-1
                            g-mr-3"></i>
                        Reply
                    </a>
                </li>
                <li class="list-inline-item ml-auto">
                <a id="full-post" class="u-link-v5 g-color-gray-dark-v4
                    g-color-primary--hover" data-id="${post.id}" href="#">
                    <i class="fa fa-reply g-pos-rel g-top-1
                        g-mr-3"></i>
                    Full Post
                </a>
                <button class="btn delete" post_id="${post_id}">Delete</button>
            </li>
            </ul>
            </div>
        </div>
            `
            // append post to UI
            document.querySelector('.row').appendChild(div)
    });
}


async function addPost(){
    
     title = document.querySelector('[name="title"]').value
     content = document.querySelector('[name="content"]').value
     author = parseInt(document.querySelector('[name="author"]').value) 

    const data = {
        method:'POST',
        headers:{
            'content-type': 'application/json'
        },
        body: JSON.stringify({
            "title": title,
            "content": content,
            "author": author
        })     
    }

    try{
        const res = await fetch('/api/post/create/', data)
        const post = await res.json()
        console.log(post)
        post_id = post.id

        // retrieve the new post
        const res2 = await fetch(`/api/post/detail/${post_id}/`)
        const post2 = await res2.json()

        
        displayPosts([post2])
    }
    catch(err){
        console.log('Error with create new Post: ', err)
    }

}

async function updatePost(){
    
    title = document.querySelector('[name="title"]').value
    content = document.querySelector('[name="content"]').value
    author = parseInt(document.querySelector('[name="author"]').value) 
    console.log(author)

   const data = {
       method:'PUT',
       headers:{
           'content-type': 'application/json'
       },
       body: JSON.stringify({
           "title": title,
           "content": content,
           "author": author
       })     
   }

   try{
       post_id = document.querySelector('form').lastElementChild.getAttribute('post-id')
       let res = await fetch(`/api/post/update/${post_id}/`, data)
       let post = await res.json()

       // retrieve the new updated post
        res = await fetch(`/api/post/detail/${post_id}/`)
        post = await res.json()

        // show a single post
        createPost(post)

   }
   catch(err){
       console.log('Error with create new Post: ', err)
   }

}


document.querySelector('form').addEventListener('click', (e) => {
    e.preventDefault()

    if(e.target.getAttribute('value') === "Post"){
        addPost()
    }
    else if (e.target.getAttribute('value') === 'Update') {
        updatePost()        
    }
});


document.querySelector('.container').addEventListener('click',  (e) => {
    e.preventDefault()
    if(e.target.classList.contains('btn') && e.target.classList.contains('delete') ){
        post_id = e.target.getAttribute('post_id') 
        e.target.parentElement.style.display = 'none'
        destroyPost(post_id)
        fetchPostsList()
    }
});

fetchPostsList()

