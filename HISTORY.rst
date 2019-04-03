History
-------

- 0.4.3 Apr 02, 2019

   -  Change "Recent Actions" to "Apps" on the apps table
   -  Fix string not being able to translate because of title-case 
   -  Instead of "My Actions" show the name/username of the current user
   -  Avoiding the overflow of links in forms; Not applying to .main a anymore because it can touch in links you don't want break-all

- 0.4.2 Mar 17, 2019

   -  Using context var app_list from Django Admin and not from our custom template tag.
   -  Custom template tag and custom template for sidebar removed, it's more simple now.
   -  available_apps now provides us a way to render the app list everywhere on Django Admin.
   -  For more: #54 #140 #141

- 0.4.1 Mar 04, 2019

   -  Fix sidebar menu too small in some screens #129
   -  Sidebar Filters are now collapsable #133
   -  Fix misaligned icons for related field
   -  Fix style of autocomplete widget
   -  Fix errors not highlighted for multiple fields per line
   -  Fix misaligned Checkboxes
   -  Small CSS fixes

- 0.4.0 Aug 31, 2018

   -   Better documentation and package info
   -   More convenient way to branding

- 0.3.9 Jan 28, 2018

   -   Now supporting Django 2.0
   -   Fixing StackedInline collapsible

- 0.3.8 Dec 1, 2017

   -   Now supporting Django 1.11 (end support for older versions)
   -   Ability to specify custom classes for admin inline fields
   -   Removing (almost all) javascript code from templates
   -   Using CDN for bootstrap files
   -   Fix widgets not rendering correctly:
       -   related lookup, add and change links
       -   split datetime
       -   raw id fields
       -   file field
       -   url field
   -   Now sidebar menu is enabled by default

- 0.3.7.1 Sep 6, 2016

   -   Fix template tag on Django 1.8.

- 0.3.7 Sep 4, 2016

   -   Better compatibility with latest Django
   -   Python 3 fix #86
   -   Upgrade to Bootstrap v3.3.7
   -   Fix some minor bugs

- 0.3.6 Apr 19, 2015

   -   Django 1.8 Compatibility #80
   -   Fix .place-info-actions height

-  0.3.5 Mar 11, 2015

   -   Fix wrong bootstrap column calculations fix for xs-sized devices #77 

-  0.3.4 Fev 18, 2015

   -   Fix #66 center calendar box caption
   -   Fix collapsable fieldsets not showing. #61
   -   Fix .field-box broken on chrome. #65
   -   Fix h2 margin top. #64
   -   Fix filter vertical breaks on chrome #63.
   -   Fix popover closes/fadeout before I can click on the link #57

-  0.3.3 Dec 2, 2014

   -   Very Important Fix: Checkbox Not showing on TabularInline

-  0.3.2 Nov 26, 2014

   -   Don't overrride default widget classes

-  0.3.1 Nov 17, 2014

   -   Completely new interface
   -   Sidebar menu with apps
   -   Support Django 1.7.*
   -   Bootstrap 3
   -   Better dashboard =]

-  0.3.0 Nov 29, 2013

   -   Fix: Fix to allow use inline forms with non editable custom pk in models ( pull #36 )
   -   Add/Fix: custom django-reversion and django-reversion-compare templates and other fixes ( pull #35 )
   -   Add: .sortoptions styling in changelist. ( pull #34 )

-  0.2.9 Nov 13, 2013

   -   Fix: Use "/" divider in breadcrumbs where "&rsaquo;" remains. ( pull #33 )

-  0.2.8 Nov 07, 2013

   -   Fix: Forgot to add README.rst on MANIFEST.in (shame on me)

-  0.2.7 Nov 07, 2013

   -   Fix: bug when retrieving message.tags ( pull #32 )

-  0.2.6 Nov 05, 2013

   -   django-mptt templates ( pull #30 )

-  0.2.5 Oct 14, 2013

   -  Enhancement: Separate field template to allow easy customizations.
      ( pull #26 )

-  0.2.4 Oct 13, 2013

   -  Fix: Do not add span8 class to inputs of CheckboxSelectMultiple. (
      pull #24 )

-  0.2.3 Oct 7, 2013

   -  Fix: Style for errors list on tabular inline.
   -  Fix: issue #22

-  0.2.2 Aug 11, 2013

   -  Fix: "shaking" effect that nav-bar causes when is affixed on top.
   -  Fix: search input width (responsive)
   -  Fix: adding overflow ellipsis on the form search input
   -  Fix: margin for "add-another" option

-  0.2.1 May 23, 2013

   -  Fix: the issue #17 (about the MANIFEST.in)

-  0.2.0 May 14, 2013

   -  Final touches
   -  Show the search input properly considering the permissions
   -  Fix: z-index nav-bar bug

-  previous versions

   -  Has some bugs, you can use, but I recommend the latest
      version.
