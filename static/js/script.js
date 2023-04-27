
async function fetchAPIData(){

    try{
        
        const res = await fetch('/api/post/')
        const posts = await res.json()
        displayPosts(posts)
    }
    catch(err){
        console.log('Error with fetch: ',err)
    }

    
}

function displayPosts(posts){
    posts.forEach((post) => {
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
                        g-color-primary--hover" href="#!">
                        <i class="fa fa-thumbs-up g-pos-rel
                            g-top-1 g-mr-3"></i>
                        178
                    </a>
                </li>
                <li class="list-inline-item g-mr-20">
                    <a class="u-link-v5 g-color-gray-dark-v4
                        g-color-primary--hover" href="#!">
                        <i class="fa fa-thumbs-down g-pos-rel
                            g-top-1 g-mr-3"></i>
                        34
                    </a>
                </li>
                <li class="list-inline-item ml-auto">
                    <a class="u-link-v5 g-color-gray-dark-v4
                        g-color-primary--hover" href="#!">
                        <i class="fa fa-reply g-pos-rel g-top-1
                            g-mr-3"></i>
                        Reply
                    </a>
                </li>
            </ul>
            </div>
        </div>
            `
            // append post to UI
            document.querySelector('.row').appendChild(div)
    });
}





fetchAPIData()

