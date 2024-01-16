document.querySelectorAll(".forum").forEach(forum => {
	const forumId = forum.dataset.forumId;
	const ratings = forum.querySelectorAll(".forum-rating");
	const likeRating = ratings[0];

	ratings.forEach(rating => {
		const button = rating.querySelector(".forum-rating-button");
		const count = rating.querySelector(".forum-rating-count");

		button.addEventListener("click", async () => {
			if (rating.classList.contains("forum-rating-selected")) {
				return;
			}

			count.textContent = Number(count.textContent) + 1;

			ratings.forEach(rating => {
				if (rating.classList.contains("forum-rating-selected")) {
					const count = rating.querySelector(".forum-rating-count");

					count.textContent = Math.max(0, Number(count.textContent) - 1);
					rating.classList.remove("forum-rating-selected");
				}
			});

			rating.classList.add("forum-rating-selected");

			const likeOrDislike = likeRating === rating ? "like" : "dislike";
			const response = await fetch(`/forums/${forumId}/${likeOrDislike}`);
			const body = await response.json();
		});
	});
});