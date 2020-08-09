Localization hand in hand with digitization
###########################################

:author: Ashwin Vishnu Mohanan
:date: 2020-08-09T12:35:20.563057
:slug: localization-digitization
:status: draft
:summary: When everything you read, write and create is digital it preserve
          culture and make it accessible
:category: Tech Talk
:tags: software


Reading in your local language
------------------------------

https://www.freedesktop.org/software/fontconfig/fontconfig-user.html

Check what is the default language::

  ❯ fc-match :lang=ml
  Meera-Regular.ttf: "Meera" "Regular"

This particular font tends to be small when inline with Latin fonts. So
following the docs_, I added this::

  <!--
         Use an SMC font when requested for Malayalam
  -->
  <match>
         <test name="lang" compare="contains">
         <string>ml</string>
         </test>
         <edit name="family" mode="prepend">
         <string>AnjaliOldLipi</string>
         </edit>
  </match>

After making this change, if we check again::

  ❯ fc-match :lang=ml
  AnjaliOldLipi-Regular.ttf: "AnjaliOldLipi" "Regular"
