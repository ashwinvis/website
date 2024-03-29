Welcome
#######

:date: 2019-11-12
:save_as: index.html
:original_url: pages/showcase.html
:summary: My blog / showcase
:url:
:cover: {static}/static/cover-light.svg
:hide_navbar_brand: True
:landing:

  .. role:: raw-html(raw)
      :format: html

  .. role:: p-org

  .. container:: h-card

    .. container:: m-row

        .. container:: m-col-l-9 m-push-l-1 m-col-m-7 m-nopadb

            .. raw:: html

                <h1 id="landing">
                  <span class="m-thin">
                    <span class="landing-prompt">❯❯❯ </span>
                    <span class="landing-kw">from</span>
                    <a class="p-name u-url" href="https://fluid.quest"><span class="landing-mod">fluid.quest</span></a>
                    <span class="landing-kw">import</span>
                    <span class="landing-mod">say</span>
                    <br/>
                  </span>
                </h1>

    .. container:: m-row

        .. container:: m-col-l-6 m-push-l-1 m-col-m-7 m-nopadt

            .. container:: m-block m-primary m-badge landing-float-right

               .. image:: /images/dp_ashwin_2016.jpg
                  :alt: Portrait of Ashwin taken in Paris, 2016

               .. raw:: html

                  <h3>
                    <code>❯❯❯ say.hello()</code>
                  </h3>
                  <p>
                    <i>Welcome!</i> My name is
                    <span class="p-given-name">Ashwin Vishnu</span>
                    <span class="p-family-name">Mohanan</span>.
                  </p>

                  <h3>
                    <code>❯❯❯ say.whoami() </code>
                  </h3>

               Academic turned research software engineer / scientific programmer / systems developer at :p-org:`SMHI`,
               blogger, husband, father and a person.
               Find more `what I do 👇`_ or
               check out my `blog posts 👉 </archives.html>`__.

               .. raw:: html

                  <h3>
                    <code>❯❯❯ continue
                       <span class="landing-ticker">|</span>
                    </code>
                  </h3>


        .. container:: m-col-l-3 m-push-l-2 m-col-m-4 m-push-m-1 m-col-s-6 m-push-s-3 m-col-t-8 m-push-t-2

            .. button-primary:: /archives.html
                :class: m-fullwidth

                Blog posts

.. _what I do 👇:

.. container:: m-container-inflate grid-item grid-row-3

   .. container:: grid-item

       .. block-success:: Curriculum Vitae

             Find out my past, present and possible futures in the
             latest iteration of ...

             .. button-primary:: {filename}/pages/cv.rst
                 :class: m-fullwidth button-down

                 My CV

   .. container:: grid-item

       .. block-warning:: Research

           A more or less up to date description of my research articles
           and talks

           .. button-primary:: {filename}/pages/research.rst
               :class: m-fullwidth button-down

               My portfolio

   .. container:: grid-item

       .. block-info:: Software

           A mix of serious and fun coding projects, mostly hosted on GitHub

           .. button-primary:: {filename}/pages/software.rst
               :class: m-fullwidth button-down

               My codes
