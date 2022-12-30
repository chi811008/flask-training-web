function delete_finger_training(finger_training_id) {
    fetch("/delete_finger_training", {
        method: "POST",
        body: JSON.stringify({ finger_training_id: finger_training_id })
    }).then((_res) => {
        window.location.href = "/";
    });
}