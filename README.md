# WP4: publish_aud_request
This repository is intended to publish AUD request to DHT to invoke the [AUD Manager](https://github.com/sifis-home/wp4-aud_manager)

Build the image using the following command:

`docker build -t publish_aud_request .`

Run the Docker container using the command shown below:

`docker run -ti --net=host publish_aud_request python -m publish_aud_request --Request status`

---
## License

Released under the [MIT License](LICENSE).

## Acknowledgements

This software has been developed in the scope of the H2020 project SIFIS-Home with GA n. 952652.
