<p align="center">
  A libopenTIDAL python wrapper.
</p>

MIT License

>  Copyright (c) 2021 Hugo Melder
>
>  Permission is hereby granted, free of charge, to any person obtaining a copy
>  of this software and associated documentation files (the "Software"), to deal
>  in the Software without restriction, including without limitation the rights
>  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>  copies of the Software, and to permit persons to whom the Software is
>  furnished to do so, subject to the following conditions:
>
>  The above copyright notice and this permission notice shall be included in
>  all copies or substantial portions of the Software.
>
>  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
>  THE SOFTWARE.

### Introduction
libopenTIDAL is a TIDAL API client library written in ANSI C. It's lightweight, fast and easy to use.

After reverse-engineering the TIDAL API and documenting all endpoints, I had the idea to write a portable C library. The goal was to integrate the OAuth2 Device-Flow, auto-refreshing sessions and all endpoints. 

A python module using openTIDAL is also available and easy to install (currently in development).

##### What is implemented?
* OAuth Log-In/Logout and Automatic Session Renewal
* Demo Session
* Playlist Creation, Deletion and Manipulation
* Mixes (also known as Radio)
* Favourites Management
* Recently Played, Your History, Because You Listened To {album} and other user-based content recommendations
* Pagination (Limit & Offset)
* Order & Sort Filters
* Content HTTP Streams (Audio & Video)
* Easy and Extensive Error Handling

### Wiki
Work in progress.

### Thread Safety
openTIDAL is thread safe.
You need to create a http-handle for a new thread.
Session refresh checks and requests are only available on the main thread.

### Building
```
$ git submodule init && git submodule update
```
```
$ pip3 install ./
```

##### Dependencies
openTIDAL uses libcURL for HTTP Requests. In modern systems curl is preinstalled (macOS, Windows 10 (1803 or later) and most Linux distributions).

You'll need the development package on some Linux distributions. The libcurl header files are bundled with the xcode command line tools on macOS.

On Debian & other APT-based Distros:
```
$ apt install libcurl-dev
```

On CentOS:
```
$ dnf install libcurl-devel
```

pyopenTIDAL uses the cffi module. This module requires a working C compiler if you build pyopenTIDAL from source.

## Disclaimer

I deeply discourage you from building and distributing copyright-infringing apps. Create something that adds up to TIDAL's Service.

## Credits
* cURL (Daniel Stenberg & Contributors)
* cJSON (Dave Gamble & Contributors)
* Base64 (The Apache Group.)
