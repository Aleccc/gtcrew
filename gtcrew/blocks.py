from wagtail.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, StructValue, PageChooserBlock
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    caption = CharBlock(required=False)
    image = ImageChooserBlock(required=True)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class GalleryBlock(StreamBlock):
    images = ImageBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/gallery_block.html'


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('display-1', 'Display 1'),
        ('display-2', 'Display 2'),
        ('display-3', 'Display 3'),
        ('display-4', 'Display 4'),
        ('display-5', 'Display 5'),
        ('display-6', 'Display 6'),
    ], blank=True, required=False)
    font_color = ChoiceBlock(choices=[
        ('', 'Default'),
        ('text-muted', 'Muted'),
        ('text-primary', 'Primary'),
        ('text-secondary', 'Secondary'),
        ('text-light', 'Light'),
        ('text-dark', 'Dark'),
    ], blank=True, required=False)
    font_alignment = ChoiceBlock(choices=[
        ('', 'Left'),
        ('text-center', 'Center'),
        ('text-right', 'Right'),
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class ParagraphBlock(StructBlock):
    body = RichTextBlock()
    font_color = ChoiceBlock(choices=[
        ('', 'Default'),
        ('text-muted', 'Muted'),
        ('text-primary', 'Primary'),
        ('text-secondary', 'Secondary'),
        ('text-light', 'Light'),
        ('text-dark', 'Dark'),
    ], blank=True, required=False)
    font_alignment = ChoiceBlock(choices=[
        ('', 'Left'),
        ('text-center', 'Center'),
        ('text-right', 'Right'),
    ], blank=True, required=False)

    class Meta:
        icon = "pilcrow"
        template = "blocks/paragraph_block.html"


class QuoteBlock(StructBlock):
    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "openquote"
        template = "blocks/quote_block.html"


class CarouselItemBlock(StructBlock):
    label = CharBlock(required=False)
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/carousel_item_block.html"


class CarouselBlock(StreamBlock):
    carousel_item_block = CarouselItemBlock()

    class Meta:
        icon = "image"
        template = "blocks/carousel_block.html"


class AccordionItemBlock(StructBlock):
    header = CharBlock(icon="title")
    body = ParagraphBlock()

    class Meta:
        icon = "list-ul"
        template = "blocks/accordion_item_block.html"


class AccordionBlock(StreamBlock):
    accordion_item_block = AccordionItemBlock()

    class Meta:
        icon = "list-ul"
        template = "blocks/accordion_block.html"


class CardBlock(StructBlock):
    header = CharBlock(icon="title", required=False)
    image = ImageChooserBlock(required=False)
    body = ParagraphBlock()

    class Meta:
        icon = "copy"
        template = "blocks/card_block.html"


class CardGridBlock(StreamBlock):
    card_block = CardBlock()

    class Meta:
        icon = "table"
        template = "blocks/card_grid_block.html"


class TimelineBlock(StreamBlock):
    timeline_entry_block = ParagraphBlock()

    class Meta:
        template = "blocks/timeline_block.html"


class HeadingGroupBlock(StreamBlock):
    heading = HeadingBlock()

    class Meta:
        icon = "Title"
        template = "blocks/heading_group_block.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_group_block = HeadingGroupBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow",
        template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="link",
        template="blocks/embed_block.html")

    class Meta:
        template = "blocks/base_stream_block.html"


class PostBlock(StructBlock):
    heading_small = CharBlock()
    heading_large = CharBlock()
    paragraph = RichTextBlock()
    photo = ImageChooserBlock(required=False)
    page = PageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)

    class Meta:
        icon = 'doc-empty'
        template = 'blocks/post_block.html'


class ColumnBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = ParagraphBlock()
    image_block = ImageBlock()
    quote_block = QuoteBlock()
    card_block = CardBlock()
    carousel_block = CarouselBlock()
    # accordion_block = AccordionBlock()
    card_grid_block = CardGridBlock()
    gallery_block = GalleryBlock()
    # timeline_block = TimelineBlock()
    post_block = PostBlock()

    class Meta:
        icon = "table"
        template = "blocks/column_block.html"


class OneColumnRowBlock(StructBlock):
    column = ColumnBlock()

    class Meta:
        template = "blocks/row_1col_block.html"


class TwoColumnRowBlock(StructBlock):
    left_column = ColumnBlock()
    right_column = ColumnBlock()
    width = ChoiceBlock(choices=[
        ('', 'Even'),
        ('-8', 'Large Left Column'),
        ('-4', 'Large Right Column'),
    ], blank=True, required=False)
    vertical_alignment = ChoiceBlock(choices=[
        ('', 'Top'),
        ('align-items-center', 'Middle'),
        ('align-items-end', 'Bottom'),
    ], blank=True, required=False)

    class Meta:
        template = "blocks/row_2col_block.html"


class RowBlock(StreamBlock):
    one_column_row_block = OneColumnRowBlock()
    two_column_row_block = TwoColumnRowBlock()

    class Meta:
        icon = "horizontalrule"
        template = "blocks/row_block.html"


class PaddingStructValue(StructValue):
    def generate(self):
        top = self.get('top', 't-3')
        bottom = self.get('bottom', 'b-3')
        left = self.get('left', 's-3')
        right = self.get('right', 'e-3')
        return f'p{top} p{bottom} p{left} p{right}'


class MarginStructValue(StructValue):
    def generate(self):
        top = self.get('top', 't-3')
        bottom = self.get('bottom', 'b-3')
        left = self.get('left', 's-3')
        right = self.get('right', 'e-3')
        return f'm{top} m{bottom} m{left} m{right}'


class PaddingBlock(StructBlock):
    top = ChoiceBlock(choices=[
        ('t-0', 'Smallest'),
        ('t-1', 'Small'),
        ('t-2', 'Medium Small'),
        ('t-3', 'Medium'),
        ('t-4', 'Large'),
        ('t-5', 'Largest'),
        ('t-auto', 'Auto'),
    ], blank=True, required=False)
    bottom = ChoiceBlock(choices=[
        ('b-0', 'Smallest'),
        ('b-1', 'Small'),
        ('b-2', 'Medium Small'),
        ('b-3', 'Medium'),
        ('b-4', 'Large'),
        ('b-5', 'Largest'),
        ('b-auto', 'Auto'),
    ], blank=True, required=False)
    left = ChoiceBlock(choices=[
        ('s-0', 'Smallest'),
        ('s-1', 'Small'),
        ('s-2', 'Medium Small'),
        ('s-3', 'Medium'),
        ('s-4', 'Large'),
        ('s-5', 'Largest'),
        ('s-auto', 'Auto'),
    ], blank=True, required=False)
    right = ChoiceBlock(choices=[
        ('e-0', 'Smallest'),
        ('e-1', 'Small'),
        ('e-2', 'Medium Small'),
        ('e-3', 'Medium'),
        ('e-4', 'Large'),
        ('e-5', 'Largest'),
        ('e-auto', 'Auto'),
    ], blank=True, required=False)

    class Meta:
        value_class = PaddingStructValue


class MarginBlock(PaddingBlock):
    class Meta:
        value_class = MarginStructValue


class SectionBlock(StructBlock):
    row = RowBlock(max_num=1)
    background_color = ChoiceBlock(choices=[
        # ('13,110,253', 'Primary'),
        # ('108,117,125', 'Secondary'),
        # ('248,249,250', 'Light'),
        # ('33,37,41', 'Dark'),
        ('bg-transparent', 'Transparent'),
        ('bg-primary', 'Primary'),
        ('bg-secondary', 'Secondary'),
        ('bg-light', 'Light'),
        ('bg-dark', 'Dark'),
    ], blank=True, required=False)
    background_image = ImageChooserBlock(required=False)
    margin = MarginBlock(required=False)
    padding = PaddingBlock(required=False)

    class Meta:
        icon = "bars"
        template = "blocks/section_block.html"
