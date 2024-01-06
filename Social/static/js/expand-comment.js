  function toggleCommentSection(postId) {
        var commentSection = document.getElementById('comment-section-' + postId);
        if (commentSection.style.display === 'none' || !commentSection.style.display) {
            commentSection.style.display = 'block';
        } else {
            commentSection.style.display = 'none';
        }
        event.preventDefault();
    }