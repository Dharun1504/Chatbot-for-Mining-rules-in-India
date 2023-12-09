css = '''
<style>
.chat-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.chat-message {
    display: flex;
    margin-bottom: 10px;
}

.chat-message.user {
    justify-content: flex-start;
}

.chat-message.bot {
    justify-content: flex-end;
}

.chat-message .avatar {
    width: 40px;
    height: 40px;
    margin-right: 10px;
    border-radius: 50%;
    overflow: hidden;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.chat-message .message {
    background-color: #000000;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    max-width: 70%;
}

.chat-message.user .message {
    background-color: #007bff;
    color: white;
    align-self: flex-end;
}

.chat-message.bot .message {
    background-color: #007bff;
    color: white;
    align-self: flex-start;
}

/* Icons for user and bot avatars */
.chat-message.user .avatar img::before {
    content: url("https://i.ibb.co/k4hYCqt/sih1.jpg"); /* Smiling Face with Open Mouth emoji */
    font-size: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.chat-message.bot .avatar img::before {
    content: "\1F916"; /* Robot Face emoji */
    font-size: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Most Used Queries Styles */
.sidebar-container {
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.sidebar-container h3 {
    color: #007bff;
    font-size: 18px;
    margin-bottom: 10px;
}
.sidebar-button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    margin: 5px 0;
    cursor: pointer;
}

.sidebar-button:hover {
    background-color: #0056b3;
}
</style>

'''

# Rest of your code remains unchanged


bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
     <div class="avatar">
        <img src="https://i.ibb.co/k4hYCqt/sih1.jpg" alt="User Avatar">
    </div>   
    <div class="message">{{MSG}}</div>
</div>
'''
