# JPConstantineau's CNCEncoderPad: A Video Editing Macropad and Jog Wheel

![CNCEncoderPad](https://cdn.tindiemedia.com/images/resize/UWexrAD9p6az5NN9XkHlDmtXHJQ=/p/fit-in/653x435/filters:fill(fff)/i/556481/products/2021-03-04T05%3A39%3A10.731Z-encoderpad.jpg?1614808472)


9-Keys Macropad with a large rotary encoder.

There are 3 versions of the EncoderPad.  Only 2 support KMK. The Basic version isn't supported due to the SAMD21 processor which has limited RAM and Flash sizes.

<table>
    <thead>
        <tr>
            <th colspan="1"></th>
            <th colspan="2">Basic</th>
            <th colspan="2">Pro/Wireless</th>
            <th>RP2040/RGB</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="1">KMK Compatible</td>
            <td colspan="2"> No</td>
            <td colspan="2"> Yes</td>
            <td colspan="1"> Yes</td>
        </tr>
        <tr>
            <td colspan="1">Compatible Board</td>
            <td>Seeeduino XIAO</td>
            <td>Adafruit QT Py</td>
            <td>BlueMicro840 Nice!Nano</td>
            <td>Pro Micro RP2040</td>
            <td>Included on PCB</td>
        </tr>
        <tr>
            <td>Processor Details</td>           
            <td>SAMD21G18</td>
            <td>SAMD21G18 </td>
            <td>nRF52840</td>
            <td>RP2040</td>
            <td>RP2040</td>
        </tr>
    </tbody>
</table>


kb_rp2040.py is designed to work with the [EncoderPad RP2040 CircuitPython UF2](https://circuitpython.org/board/jpconstantineau_encoderpad_rp2040/)
kb_BlueMicro840.py is designed to work with the [BlueMicro840 CircuitPython UF2](https://circuitpython.org/board/bluemicro840/)
kb_ProMicroRP2040.py is designed to work with the [Sparkfun Pro Micro RP2040 CircuitPython UF2](https://circuitpython.org/board/sparkfun_pro_micro_rp2040/)

Retailers (USA)  
[BlueMicro Store on Tindie - Wireless/Pro](https://www.tindie.com/products/jpconstantineau/wireless-video-editing-macropad-and-jog-wheel/)

Extensions enabled by default  
- [Layers](https://github.com/KMKfw/kmk_firmware/tree/master/docs/layers.md) Need more keys than switches? Use layers.
- [RGB](https://github.com/KMKfw/kmk_firmware/tree/master/docs/rgb.md) Light it up
- [MediaKeys](https://github.com/KMKfw/kmk_firmware/tree/master/docs/media_keys.md) Control volume and other media functions
