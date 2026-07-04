<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aliadde/Yt_Telegram_Downloader">
    <img src="images/logo.png" alt="Logo" width="200" height="160">
  </a>

<h3 align="center"> Youtube Telegram Downloader</h3>

  <p align="center">
    Use this project to downloader from youtube a list of youtube video link['s].
    <br />
    <a href="https://github.com/aliadde/Yt_Telegram_Downloader"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    &middot;
    <a href="https://github.com/aliadde/Yt_Telegram_Downloader/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/aliadde/Yt_Telegram_Downloader/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](./images/screenshot.png)
There are many good Youtube video downloader. But this automation tools work with list of links you give it or you may like only one video. It uses your telegram account **app api id** and **app ai hash** to connect to your account and then send message to a telegram bot **@YoutubeFiler_bot**

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python3]][Python-url]
* [![Telethon][Telethon-url]][Telethon-link]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Getting Started

To run this project, you will need your Telegram account's **API ID** and **API Hash**. 

> 💡 **Note:** This Bot **@YoutubeFiler_bot** may have advertising channel that ask you to join this channel. so, before starting downloading your youtube video you must ensure that one you join to these channel and clicking on button "جوین شدم". after that you are free to automate download.

### Prerequisites

* **Python 3.11+** installed on your system.
* A Telegram account to get your API credentials:
  1. Go to [my.telegram.org](https://my.telegram.org/) and log in.
  2. Navigate to **API development tools**.
  3. Create a new application to obtain your `App api_id` and `App api_hash`.

> 💡 **Note:** Don't worry—you only need to enter these credentials once. After the initial setup, the script will generate a `.session` file to keep you logged in securely.

### Installation
### Installation

Choose the installation method that matches your operating system:

#### 📂 Option 1: Linux / macOS (Manual Installation)

1. Clone the repository:
  ```sh
   git clone git@github.com:aliadde/Yt_Telegram_Downloader.git
  ```
2. Navigate to the project directory and set up a virtual environment:
  ```sh
    cd Yt_Telegram_Downloader/
    python3 -m venv .venv
    source .venv/bin/activate
  ```
3. Install the required packages:
   ```sh
     pip install -r requirements.txt
   ```
4. Run the application:
   ```python
    python3 main.py
   ```

#### 🪟 Option 2: Windows (Automated or Manual)

Automated Setup:
Simply run the setup batch file in your terminal:
```cmd
  ./setup.bat
```
> 💡 **Note** for Windows Users: If you prefer manual installation, you can follow the same steps as the Linux/macOS guide above. Just make sure to activate your virtual environment using .venv\Scripts\activate instead of the source command.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### 💡 Important Note on Video Quality
For simplicity and faster automation, the script automatically defaults to **720p video quality** if it is available in the Telegram bot's inline keyboard buttons. If 720p is not available, it will automatically select the very first option/button provided by the bot.

There are two primary ways to use this application depending on your needs.

> 📂 **Default Output Directory:** By default, downloaded videos are saved in the `/static/` folder of the project directory.

### 1. Download a Single Video

To download a single YouTube video, use the `-l` flag:
```sh
python3 main.py -l <your_video_link>

```

If you want to save the video to a specific directory instead of the default folder, add the `-o` flag with your custom path:

```sh
python3 main.py -l <your_video_link> -o </path/to/output/dir/>

```


### 2. Download Multiple Videos (Bulk Download)

If you have a list of YouTube videos you want to download all at once, use the following command:

```sh
python3 main.py  [ -o </path/to/output/dir/> ]  <path_to_links_file.txt>
```
*(Make sure to create a text file containing one YouTube link per line.)*


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="git@github.com:aliadde/Yt_Telegram_Downloader.git/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

X Account - [@Aliad1913](https://x.com/Aliad1913) - 

Project Link: [Yt_Telegram_Downloader](https://github.com/aliadde/Yt_Telegram_Downloader)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python3]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Telethon-url]: https://img.shields.io/badge/Telethon-blue?style=for-the-badge&logo=telegram&logoColor=white
[Telethon-link]: https://github.com/LonamiWebs/Telethon