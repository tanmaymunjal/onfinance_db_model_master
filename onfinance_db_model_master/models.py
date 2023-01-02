import re
from bson import DBRef
from mongoengine import Document, EmailField, BinaryField, DynamicField
from mongoengine import DateTimeField, EmbeddedDocument, StringField, URLField
from mongoengine import ReferenceField, EmbeddedDocumentListField, ListField
from mongoengine import IntField, FloatField, BooleanField, DateField, DictField

class Secrets(Document):
    apiKey = StringField()
    zerodha_username = StringField()
    zerodha_password = StringField()
    zerodha_2fa = StringField()
    apiSecrets = StringField()
    accessToken = StringField()
    accountName = StringField()

class Webinar(Document):
    webinar_name = StringField(required=True, unique=True)
    webinar_url = URLField(required=True)
    webinar_image_url = URLField(required=True)
    webinar_metadata = ListField(StringField)



class Communities(Document):
    community_name = StringField(required=True, unique=True)
    community_image_url = URLField(required=True)
    community_url = URLField(required=True)
    community_admin_name = StringField(required=True)
    community_metadata = ListField(StringField)


class Discussions(EmbeddedDocument):
    discussion_author_img = StringField(required=True)
    discussion_author_name = StringField(required=True)
    discussion_author_username = StringField(required=True)
    discussion_content = StringField(required=True)
    discussion_platform = StringField(
        required=True, choices=["Reddit", "Twitter", "Telegram", "Discord"]
    )
    published_date = DateField()
    total_engagement = IntField()
    discussion_url = URLField()
    discussion_sentiment = FloatField()
    discussion_tags = ListField(StringField)


class ExpertOutlooks(EmbeddedDocument):
    expert_name = StringField(required=True)
    recommendation_time = DateField(required=True)
    recommended_price = FloatField()
    current_returns = FloatField()
    tip_rationale = ListField(StringField)
    target_price = FloatField()
    stoploss_price = FloatField()
    timeframe = StringField()
    expert_recommendation = StringField(choices=["BUY", "HOLD", "SELL"])


class PurchaseOption(EmbeddedDocument):
    link = URLField()
    name = StringField()
    icon = URLField()
    spread = FloatField()
    volume = FloatField()
    price = FloatField()


class SubDiscussions(EmbeddedDocument):
    author_name = StringField()
    published_date = DateTimeField()
    num_likes = IntField(default=0)
    comment_text = StringField()


class NewDiscussionsTag(EmbeddedDocument):
    tag_type = StringField()
    tag_content = StringField()
    tag_metadata = StringField()


class NewDiscussions(Document):
    og_platform = StringField()
    entity_name = StringField(required=True)
    author_name = StringField()
    author_profile_pic = StringField()
    comment_text = StringField(required=True)
    published_date = DateField()
    tags = EmbeddedDocumentListField(NewDiscussionsTag)
    num_likes = IntField(default=0)
    num_comments = IntField(default=0)
    sub_comments = EmbeddedDocumentListField(SubDiscussions)


class Entity(Document):
    entity_type = StringField(required=True, choices=["equity", "crypto"])
    entity_name = StringField(required=True)
    entity_ticker = StringField(required=True)
    entity_ticker_alt = StringField()
    entity_icon_url = URLField()
    entity_index = ListField(StringField())
    entity_sector = StringField()
    fundamental_analysis = DynamicField()
    technical_analysis = DynamicField()
    important_links = DynamicField()
    purchase_options = EmbeddedDocumentListField(PurchaseOption)
    social_discussions = EmbeddedDocumentListField(Discussions)
    stock_tips = EmbeddedDocumentListField(ExpertOutlooks)
    data_feed = URLField()
    entity_fb_id = StringField()
    is_entity_complete = BooleanField()
    entity_ecosystem = StringField(
        choices=["Ethereum", "BSC", "Polygon", " Avalanche", "Fantom"]
    )
    entity_ecosystem_rank = IntField()
    entity_exchange = StringField()
    tag = StringField(choices=["top gainer", "top loser", "spotlight"])
    tag_validity = DateTimeField()

class RawInsights(Document):
    insight_title = StringField(unique=True, required=True)
    insight_description = StringField()
    insight_published_date = DateTimeField()
    insight_publish_price = FloatField()
    insight_read_time = IntField()
    insight_source = StringField()
    insight_img_url = URLField()
    insight_source_page_url = URLField()
    insight_event_group = StringField()
    insight_signal_sentiment = FloatField()
    insight_entity_sentiment = FloatField()
    insight_event_sentiment = FloatField()
    insight_signal_relevance = FloatField()
    insight_entity_relevance = FloatField()
    insight_event_relevance = FloatField()
    insight_order = FloatField()
    insight_entity_id = StringField()
    insight_entity_name = StringField()
    insight_entity_index = StringField()
    insight_entity_sector = StringField()
    insight_entity_ticker = StringField()
    insight_entity_logo = StringField()
    insight_entity_type = StringField(choices=["crypto", "equity"])
    meta = {"collection": "insights_raw"}

class RawInsightsCrypto(Document):
    insight_title = StringField(unique=True, required=True)
    insight_description = StringField()
    insight_published_date = DateTimeField()
    insight_publish_price = FloatField()
    insight_read_time = IntField()
    insight_source = StringField()
    insight_img_url = URLField()
    insight_source_page_url = URLField()
    insight_event_group = StringField()
    insight_signal_sentiment = FloatField()
    insight_entity_sentiment = FloatField()
    insight_event_sentiment = FloatField()
    insight_signal_relevance = FloatField()
    insight_entity_relevance = FloatField()
    insight_event_relevance = FloatField()
    insight_order = FloatField()
    insight_entity_id = StringField()
    insight_entity_name = StringField()
    insight_entity_index = StringField()
    insight_entity_sector = StringField()
    insight_entity_ticker = StringField()
    insight_entity_logo = StringField()
    insight_entity_type = StringField(choices=["crypto", "equity"])
    meta = {"collection": "insights_raw_crypto"}


class Insights(Document):
    insight_title = StringField(unique=True, required=True)
    insight_description = StringField()
    insight_published_date = DateTimeField()
    insight_publish_price = FloatField()
    insight_read_time = IntField()
    insight_source = StringField()
    insight_img_url = URLField()
    insight_source_page_url = URLField()
    insight_event_group = StringField()
    insight_signal_sentiment = FloatField()
    insight_entity_sentiment = FloatField()
    insight_signal_relevance = FloatField()
    insight_event_sentiment = FloatField()
    insight_order = FloatField()
    insight_entity_id = StringField()
    insight_entity_name = StringField()
    insight_entity_index = StringField()
    insight_entity_sector = StringField()
    insight_entity_ticker = StringField()
    insight_entity_logo = StringField()
    insight_entity_type = StringField(choices=["crypto", "equity"])
    insight_likes = IntField(default=0)
    meta = {
        "indexes": [
            {
                "fields": ["$insight_title", "$insight_description"],
                "default_language": "english",
            }
        ]
    }

    def fetch_insights_as_dict(
        self, user_insights_bookmarked=None, is_search_res=False
    ):
        first_split_pos = re.search("//", self.insight_source)
        market_impact_opt = ["Low", "Medium", "High"]
        if first_split_pos is not None:
            self.insight_source = self.insight_source[first_split_pos.end() :]
        secnd_split_pos = re.search("[^A-Za-z0-9.]", self.insight_source)
        if secnd_split_pos is not None:
            self.insight_source = self.insight_source[: secnd_split_pos.start()]

        user_insights_bookmarked = user_insights_bookmarked

        bookmarked = True
        if user_insights_bookmarked is not None:
            bookmarked = False
            for i in range(len(user_insights_bookmarked)):
                if str(self.id) == str(user_insights_bookmarked[i]["insight_id"].id):
                    bookmarked = True
                    break

        resp = {
            "insights_id": str(self.id),
            "insights_name": self.insight_title,
            "tag": self.insight_event_group,
            "insights_icon":self.insight_img_url,
            "entity": {
                "id": self.insight_entity_id,
                "ticker": self.insight_entity_ticker,
                "logo": self.insight_entity_logo,
            },
            "read_time": self.insight_read_time,
            "days": self.insight_published_date.isoformat(),
            "bookmarked": bookmarked,
            "event_group": self.insight_event_group,
            "entity_sentiment": self.insight_entity_sentiment,
            "projected_market_impact": market_impact_opt[
                int(self.insight_order//3334)
            ],
            "article_sentiment": self.insight_event_sentiment,
            "insight_likes": 0 if self.insight_likes is not None else self.insight_likes
        }
        if is_search_res:
            resp["result_type"] = "insight"
        return resp

    def fetch_insights_as_dict_full(self,user_insights_bookmarked=None, is_search_res=False):
        market_impact_opt = ["Low", "Medium", "High"]
        entity = Entity.objects(id=self.insight_entity_id).only("entity_fb_id").first()

        user_insights_bookmarked = user_insights_bookmarked

        bookmarked = False
        if user_insights_bookmarked is not None:
            bookmarked = False
            for i in range(len(user_insights_bookmarked)):
                if str(self.id) == str(user_insights_bookmarked[i]["insight_id"].id):
                    bookmarked = True
                    break
        resp= {
            "insight_id": str(self.id),
            "insight_name": self.insight_title,
            "insight_icon": self.insight_img_url,
            "tags": {
                "event_type": self.insight_event_group,
                "entity_name": self.insight_entity_name,
                "entity_index": [self.insight_entity_index if self.insight_entity_index is not None else "crypto"][0],
            },
            "entity": {
                "id": self.insight_entity_id,
                "ticker": self.insight_entity_ticker,
                "logo": self.insight_entity_logo,
                "firebase_price_identifier": entity.entity_fb_id,
                "entity_type": self.insight_entity_type
            },
            "read_time": self.insight_read_time,
            "publish_date": self.insight_published_date,
            "bookmarked": bookmarked,
            "description": self.insight_description,
            "read_more": self.insight_source_page_url,
            "projected_market_impact": market_impact_opt[
                int(self.insight_order//3334)
            ],
            "article_sentiment": self.insight_event_sentiment,
            "portfolio_exposure": "-",
            "days": self.insight_published_date.isoformat(),
            "entity_sentiment": self.insight_entity_sentiment,
            "price_publication": self.insight_publish_price,
            "insight_likes": 0 if self.insight_likes is not None else self.insight_likes
        }
        if is_search_res:
            resp["result_type"] = "insight"
        return resp


class InsightsRead(EmbeddedDocument):
    insight_id = ReferenceField(Insights, required=True)
    invocation_timestamp = DateField(required=True)


class InsightsBookmarked(EmbeddedDocument):
    insight_id = ReferenceField(Insights, required=True)
    invocation_timestamp = DateField(required=True)


class EntitiesExplored(EmbeddedDocument):
    entity_id = ReferenceField(Entity, required=True)
    invocation_timestamp = DateField(required=True)


class EntitiesWatchlisted(EmbeddedDocument):
    entity_id = ReferenceField(Entity, required=True)
    invocation_timestamp = DateField(required=True)


class Holdings(EmbeddedDocument):
    purchased_instrument = ReferenceField(Entity, required=True)
    purchase_platform = StringField(required=True)
    purchase_time = DateField(required=True)
    purchase_price = FloatField(required=True)
    purchase_qty = FloatField(required=True)
    portfolio_exposure = FloatField()

    def process_holding_as_dict(self, instrument_type):
        
        if isinstance(self.purchased_instrument, DBRef):
            self.purchased_instrument = Entity.objects(
                id=self.purchased_instrument
            ).first()
        data = {
            "purchase_platform": self.purchase_platform,
            "avg_purchase_price": self.purchase_price,
            "purchase_qty": self.purchase_qty,
            "firebase_path": self.purchased_instrument.entity_fb_id,
            "entity_name": self.purchased_instrument.entity_name,
            "entity_logo": self.purchased_instrument.entity_icon_url,
            "entity_id": str(self.purchased_instrument.id),
            "entity_type": self.purchased_instrument.entity_type,
            "entity_ticker": self.purchased_instrument.entity_ticker,
        }
        if instrument_type is not None and instrument_type != self.purchased_instrument.entity_type:
            return None
        return data


class User(Document):
    user_email = EmailField()
    user_phone_number = StringField()
    user_password = BinaryField()
    user_full_name = StringField(required=True)
    user_permission_level = StringField(
        default="Unauthorized", choices=["Unauthorized", "Authorized", "Admin"]
    )
    referee = StringField()
    user_debank_url = URLField()
    user_binance_auth_creds = DynamicField()
    user_entities_watchlisted = EmbeddedDocumentListField(
        EntitiesWatchlisted, default=list
    )
    user_insights_bookmarked = EmbeddedDocumentListField(
        InsightsBookmarked, default=list
    )
    user_entities_explored = EmbeddedDocumentListField(EntitiesExplored, default=list)
    user_insights_read = EmbeddedDocumentListField(InsightsRead, default=list)
    user_portfolio_holdings = EmbeddedDocumentListField(Holdings, default=list)
    notification_topic_subscriptions = ListField(StringField, default=list)
    insights_preferences = ListField(StringField, default=list)
    user_arrival_origin = StringField()
    account_creation_date = DateField()
    smallcase_id = StringField()
    profile_pic_url = URLField()
    profile_answers = DynamicField()
    user_first_auth = StringField()
    user_crypto_portfolio_value = FloatField()
    user_equity_portfolio_value = FloatField()
    user_crypto_portfolio_percentage_change = FloatField()
    user_equity_portfolio_percentage_change = FloatField()
    smallcase_lead_id = ListField(StringField)


class Notifications(Document):
    notif_title = StringField(required=True)
    notif_description = StringField(required=True)
    notif_icon = URLField()
    notif_publish_time = DateField()
    # notif_recievers = ListField(EmailField, default=list)
    notif_type = StringField(required=True)
    notif_priority = StringField(required=True, choices=["high", "medium", "low"])
    notif_entity_mentioned = ReferenceField(Entity)
    notif_image = URLField()
    
    def fetch_notif_as_dict(self):
        notif = {
            "notification_class": self.notif_type,
            "notification_content": [self.notif_title if self.notif_description == "" else self.notif_description][0],
            "notification_priority": self.notif_priority,
            "notification_date": self.notif_publish_time.isoformat(),
            "notification_title": self.notif_title
        }
        try:
            notif["entity_mentioned"] = {
                "_id": self.notif_entity_mentioned.id,
                "entity_ticker": self.notif_entity_mentioned.entity_ticker,
                "entity_logo": self.notif_entity_mentioned.entity_icon_url,
            }

        except Exception:
            try:
                notif["entity_mentioned"] = (
                    Entity.objects(id=self.notif_entity_mentioned)
                    .only("id", "entity_ticker", "entity_icon_url")
                    .first()
                    .to_mongo()
                    .to_dict()
                )
                notif["entity_mentioned"]["entity_logo"] = notif["entity_mentioned"][
                    "entity_icon_url"
                ]
            except Exception:
                notif["entity_mentioned"] = {
                    "_id": "",
                    "entity_ticker": "",
                    "entity_logo": "",
                }

        notif["entity_mentioned"]["_id"] = str(notif["entity_mentioned"]["_id"])

        return notif


class Feedback(Document):
    feedback_text = StringField()
    feedback_datetime = DateTimeField()
    feedback_uid = StringField()


class Reward(Document):
    winning_user = StringField()
    reward_amount = IntField(required=True)
    reward_platform = StringField(required=True)
    reward_coupon_code = StringField(required=True, unique=True)
    og_entry_date = DateTimeField(required=True)
    winning_date = DateTimeField()
    reward_win_reason = StringField(required=True, default="referral")
    reward_logo_url = StringField(required=True)
    has_scratched = BooleanField(required=True, default=False)
