Changelog
=========

1.4.1 (unreleased)
~~~~~~~~~~~~~~~~~~

- Prevent a ``MissingValue`` to crash the archive portlet.
  [jensens]


1.4.0 (2019-02-13)
~~~~~~~~~~~~~~~~~~

- Drop support for Plone 4.0-4.2 and Python 2.6.
  Wont test on those.
  [jensens]

- Fix broken portlet if blog_path is non existent.
  [jensens]

- Fix migration for sites w/o default folderish types available.
  [jensens]


1.3.3 (2013-08-29)
~~~~~~~~~~~~~~~~~~

- Added more strings classifiers items for this package
  [macagua]

- Updated Spanish translation
  [macagua]

- plone 4.3 compat
  [kiorky]

- Refresh buildout infra
  [kiorky]

- Move to github
  [kiorky]


1.3.2 (2012-07-17)
~~~~~~~~~~~~~~~~~~

- Added option to set entry layout to AutoBlog rule. ObjectInitialized subscriber may be
  invoked before the autoblog rule so the layout might not be set.
  [naro]


1.3.1 (2012-06-12)
~~~~~~~~~~~~~~~~~~

 - discussion Item based comments support replaced by p.a.discussion commments one - fixes: #26
   [lzdych]

 - updated template variables [lzdych]

 - updated translation for pt-br [lepri]

 - added metadata 'total_comments' in setuphandlers [lepri]

1.3 (2011-10-05)
~~~~~~~~~~~~~~~~

 - Use cropText instead of custom cropping method. cropText is smarter and unicode aware.
   [naro]
 - added conditional import for plone 4.1 compatibility
   [redcor]

 - added <include package="Products.CMFCore" /> to make it plone 4.1 compatible
   [redcor]

 - Fixed fuzzy (and broken) dutch translations
   [maerteijn]

 - Added missing normalizeString declaration (Plone4)
   [naro]

1.2 (2010-11-26)
~~~~~~~~~~~~~~~~~~~

- added Spanish translation [marcosfromero]
- changed filter toolbar for a filter portlet. GS upgrade step to automatically create a portlet when filter
  toolbar was enabled. [marcosfromero]
- filter improvements: now it's a fieldset, with a "Clear filter" link. It filters with AJAX. Changed "POST"
  method for "get" - fixes: #21 [marcosfromero]
- fixed installation in Plone 4.0 [khink, erico_andrei, yurj]
- added german translation by Hartmut Goebel - closes: #17 [lzdych]
- added patch by Hartmut Goebel for help page - closes: #18 [lzdych]
- sharing portlet now respects services order + added sharing feature to blog view - closes: #16 [lzdych]
- minor change in sharing portlet edit form - closes: #14 [lzdych]
- minor improvements of manage portlet [lzdych]
- Updated Dutch translations [jaroel]

1.1 (2010-05-12)
~~~~~~~~~~~~~~~~~~~

- Avoid ZeroDivisionError when the filter_cache field is 0 (simply do not cache then). [maurits]
- image and newsitem fancyboxes replaced by overlays - fixes: #6 [lzdych]
- enabled "Display menu" for blogs and entries [lzdych]
- added styles for sunburst Plone theme [lzdych]
- added Catalan translation by Sebas Vila-Marta [lzdych]
- removed gallery view use for example: "collective.prettyphoto" instead [lzdych]

1.0 (2010-05-03)
~~~~~~~~~~~~~~~~~~~

- minor fixes in the templates to support collective.collage.blogging extension [lzdych]
- blog's title and description can be hidden in the blog view by new option in the blog's settings [lzdych]

1.0rc3 (2010-04-26)
~~~~~~~~~~~~~~~~~~~

- Changed batch_size field UI from a selection widget to a more flexible
  entry field.  Also helps to avoid a problem with the handling of integer
  vocabularies for the selection widget. [newbery]
- Fixed error in filtering per month.
  Hopefully fixes http://plone.org/products/collective.blogging/issues/3
  [maurits]
- blog entry author's link can now optionally target to any referencable object instead of default
  author's page [lzdych]
- added Japanese translation by Yusuke Nakai [lzdych]
- cache interval for the filter toolbar dropdowns configurable in the blog (folder) settings [lzdych]

1.0rc2 (2010-02-24)
~~~~~~~~~~~~~~~~~~~

- made entry's document byline block easier to customize in the blog view [lzdych]
- updated i18n and czech translation [lzdych]

1.0rc1 (2010-02-16)
~~~~~~~~~~~~~~~~~~~

- added blogger's name field to blog entry's schemata [lzdych]
- updated czech translation [lzdych]
- cleaned up translation from blogging help page mess, so user's guide is no more translatable and will be replaced by online documentation in final version [lzdych]
- added new blog option which enables blogger to set max. length of entry's description displayed in non-full blog view [lzdych]
- auto-blogging content rule now can (optionally) enable blogging, comments, exclude from nav [lzdych]
- added new richtext field to blogs (hidden if blog content already has "text" field) [lzdych]
- added patch fixing reply counts if discussion moderation is enabled via quintagroup.plonecomments [lzdych]
- updated portuguese translation [davilima6]
- Plone 3.2 compatibility [naro]

1.0b4 (2010-01-09)
~~~~~~~~~~~~~~~~~~

- fixed unindexed blogging content by package reinstallation [lzdych]
- blog link from manage portlet excluded in the blog context [lzdych]
- blogging permission is now acquired by default [lzdych]
- unified entry rendering in blog and entry view [lzdych]
- moved blog and entry view snippets into separated macros [lzdych]
- added pictures folder reference to manage blog portlet [lzdych]
- enabled text contents of smart folders in blog view (if nonempty) [lzdych]
- fixed i18n markup for read more link [lzdych]
- added share entry portlet [lzdych]
- blog filter toolbar options now reflects blog contents [lzdych]
- blog now can show number of posts in it [lzdych]
- added dutch translation [robgietema]
- updated italian translation [luthy]
- added portuguese translation [davilima6]

1.0b3 (2009-12-06)
~~~~~~~~~~~~~~~~~~

- removed thumbnail layout replacement for blog galleries - fixes: package reinstall removes blog gallery layouts [lzdych]
- updated user's guide, i18n and czech translateion [lzdych]
- news item image box moved above entry description so it floats next to it [lzdych]
- permalink moved to document by line area [lzdych]
- added read more link to entry footer in the blog view (not for editors) [lzdych]
- new blog option available to enable / disable entry's text body rendering in the blog view [lzdych]

1.0b2 (2009-12-06)
~~~~~~~~~~~~~~~~~~

- blog view and next / prev navigation now uses EffectiveDate rather then Date sort criterion [lzdych]
- added uninstall profile (wired up with QI) [lzdych]
- next / prev navigation always enabled for blogs based on Large Folders [lzdych]
- unified entry documentbyline and keywords info and added entry footer panel to its detail [lzdych]
- fixed broken news item based entry's layout by non-closed div element of fancy box [lzdych]
- enabled blogging for ATBlog based content - makes image and file posting available in plone 4 [lzdych]
- fixed broken browser views in plone 4 by obsolete global variables usage [lzdych]
- content rule action registered for all events - fixes: zope won't start with plone4 [lzdych]
- updated i18n and czech translation [lzdych]
- removed enforce vocabulary check for blog's batch_size field - fixes: can't translate bloggable content [lzdych]

1.0b1 (2009-12-03)
~~~~~~~~~~~~~~~~~~

- updated user's guide [lzdych]
- disallow javascript resource merging - fixes: Gallery view doesn't work for anonymous sometimes [lzdych]
- updated i18n and czech translation [lzdych]
- refactored blog content markup by removing individual content type markup interfaces and added upgrade step, also fixes: missing NewsItem's title image in blog and entry view [lzdych]
- schema extenders made browser layer specific using new blogging layer [lzdych]
- browser views and static resources now hangs on new blogging specific browser layer [lzdych]
- added edit link to the entry snippet footer in the blog view [lzdych]
- extended manage blog portlet's settings by optional reference to user defined drafts link [lzdych]
- added blog archive portlet (requires publish_year and publilsh_month catalog reindex) [lzdych]
- improved browser views to enable maps to be hidden if not used [lzdych]
- removed empty entry description element if no description available [lzdych]
- added initial italian translation [luthy]

1.0a2 (2009-11-22)
~~~~~~~~~~~~~~~~~~

- updated user's guide [lzdych]
- added TTW configuration for blog view (batch size, enable toolbar) [lzdych]
- blog related fields moved to new schemata fieldset "blog" [lzdych]
- added content rules action for to enable content auto-blogging [lzdych]
- added support for bloggingmaps extension [lzdych]
- named schema extenders to avoid adaptation conflicts [lzdych]
- added support for event based blog entries [lzdych]
- unified position of entry description in blog and entry views [lzdych]
- fixed duplicated appearance of manage portlet and missing default english labels in multilingual sites [lzdych]
- remote_url made hidden in the entry and blog view if content has default value http:// [lzdych]
- portlet's link are now generated from selected addable types in its settings [lzdych]
- the blog view now renders related items of listed entries (if available) [lzdych]
- updated czech translation (most of the user's guide still not translated) [lzdych]


1.0a1 (2009-11-17)
~~~~~~~~~~~~~~~~~~

- Initial release
