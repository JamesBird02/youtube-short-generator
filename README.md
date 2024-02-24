<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JamesBird02/youtube-short-generator.git">
    <img src="images/logo.jpg" alt="Logo" width="320" height="320">
  </a>

<h3 align="center">AI Generated Youtube Shorts</h3>

  <p align="center">
    Simple program that scrapes chosen subreddit for video ideas and generates them using the OpenAI API and elevenlabs text to speech.
    <br />
    <a href="https://github.com/JamesBird02/youtube-short-generator.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JamesBird02/youtube-short-generator.git">View Demo</a>
    ·
    <a href="https://github.com/JamesBird02/youtube-short-generator.git/issues">Report Bug</a>
    ·
    <a href="https://github.com/JamesBird02/youtube-short-generator.git/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

After seeing how low effort some online short form content can be, I decided to make things worse by creating this program. With the click of a few buttons even **you** can now dilute the online space with even more pointless videos. Through automating the idea generation as well as narration and video, you have no excuse not to be mass producing content online.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.



1. Get API Keys for OpenAI (paid), Reddit and ElevenLabs 

2. Clone the repo
   ```sh
   git clone https://github.com/JamesBird02/youtube-short-generator.git
   ```
3. Install required Python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API keys and information in `.env` 
   ```python
    OPEN_AI_KEY = ""
    my_client_id=""
    my_client_secret= ""
    my_user_agent=""
    my_username=""
    my_password=""
    eleven_labs_key = ''
    subreddit = ''
   ```
5. Run in terminal
    ```cmd
     python3 src/generator.py
    ```

6. See your saved video in generated!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Generated Captions
- [ ] Automatic Upload to YouTube
- [ ] Image generation

See the [open issues](https://github.com/JamesBird02/youtube-short-generator.git/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
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

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- CONTACT -->
## Contact

James._1@outlook.com

Project Link: [https://github.com/JamesBird02/youtube-short-generator.git](https://github.com/JamesBird02/youtube-short-generator.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JamesBird02/youtube-short-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/JamesBird02/youtube-short-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JamesBird02/youtube-short-generator.svg?style=for-the-badge
[forks-url]: https://github.com/JamesBird02/youtube-short-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/JamesBird02/youtube-short-generator.svg?style=for-the-badge
[stars-url]: https://github.com/JamesBird02/youtube-short-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/JamesBird02/youtube-short-generator.svg?style=for-the-badge
[issues-url]: https://github.com/JamesBird02/youtube-short-generator/issues
[license-shield]: https://img.shields.io/github/license/JamesBird02/youtube-short-generator.svg?style=for-the-badge
[license-url]: https://github.com/JamesBird02/youtube-short-generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jamesbird0102
[product-screenshot]: images/screenshot.png