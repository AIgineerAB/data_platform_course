# Setup docker

**This video describes setting up docker in a windows machine**

<a href="https://youtu.be/Ds1S725l_EE" target="_blank">
<img src="https://github.com/kokchun/assets/blob/main/data_platform/.png?raw=true" alt="docker setup" width="600">
</a>

## Windows

1. Start with [download and install docker desktop on windows](https://docs.docker.com/desktop/setup/install/windows-install/)
 
2. Check that the installation works by opening up docker desktop and there is no error 

3. Then try out the commands in powershell or git bash 

```bash
docker ps
```

This should list out all containers, however you don't have any containers, so if you get an output like this:

`CONTAINER ID   IMAGE             COMMAND                  CREATED       STATUS                            PORTS                    NAMES`

it works properly. Also in git bash or powershell do this to see if docker installed wsl for you 

```bash
wsl --list
```

If 2-3 failed you need to install wsl manually. 

1. Install Windows Subsystem for Linux (WSL), which is a Open up powershell and type

```bash
wsl --install
```

2. Restart computer and then wsl.exe will download ubuntu.

> [!NOTE]
> it might say something like this
>
> ```
> WslRegisterDistribution failed with error: 0x80370102
>Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.
> ```
>
> this means that you need to go into BIOS settings and enable virtualization in order for windows to be able to have virtual machine natively, which ubuntu is in this case  

3. If you don't get the error go check if docker works. If you get that virtualization error go into BIOS and turn on virtualization. To do this, restart your computer and press Del, F2, F10, or Esc repeatedly to get into BIOS. It's different for different vendors but these are some common keys to try. 

4. Now go to advanced tab and select virtualization aqnd enable.

5. Save and reboot computer.








## Other videos 📹

## Read more 👓
